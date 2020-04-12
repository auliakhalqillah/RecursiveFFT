# Fast Fourier Transfrom by using recursive method
# Written by        : Aulia Khalqillah,S.Si.,M.Si
# Date              : April, 12th 2020
# Contact           : auliakhalqillah.mail@gmail.com
import timeit
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import math

def twiddle(N):
    return np.exp(-2j*np.pi/N)

def mydft(x,nf=int()):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    # Check the exist of number of sample (nf)
    if nf == 0:
        nf = N
    elif N < nf:
        rs = np.zeros(nf-N)
        x = np.concatenate([x,rs])
        nf = len(x)
        N = nf
    else:
        nf = nf
        N = nf

    # Check the number of sample (nf) is power of two or not
    pw = math.log(nf,2)
    if pw.is_integer() == False:
        rpw = round(pw)
        nf = 2**rpw
        if N >= nf:
            print("Length of data is not power of two. Its was decreased to %d" % nf)
            x = x[0:nf]
            N = nf
        else:
            print("Length of data is not power of two. Its was increased to %d" % nf)
            res = np.zeros(nf-N)
            x = np.concatenate([x,res])
            N = x.shape[0]
    else:
        nf = int(2**pw)
        x = x[0:nf]
        N = nf

    # Recursive of DFT (Cooley-Tukey Algorithm)
    if N <= 32:
        x = np.asarray(x, dtype=float)
        N = x.shape[0]
        n = np.arange(N)
        m = n.reshape((N, 1))
        YC = np.cos((2*np.pi*m*n/N))
        YS = np.sin((2*np.pi*m*n/N))
        Y = YC-(YS*1j)
        Y = np.dot(Y,x)
        return Y
    else:
        evendata = mydft(x[::2])
        odddata = mydft(x[1::2])
        fac = twiddle(N)**(np.arange(N))
        firsthalf = evendata+(fac[:int(N/2)]*odddata)
        secondhalf = evendata+(fac[int(N/2):]*odddata)
        return np.concatenate([firsthalf,secondhalf])

# Generating Random Signal
f1 = 20
n = 1000
dt = 0.01
t = np.arange(0,n)*dt
signal = np.sin(2*np.pi*f1*t)
data = signal*np.random.random(n)
N = len(data)

# Setting the frequency
nfft = 1024
freq = np.arange(0,nfft)/(nfft*dt)

print("myDFT")
mag_mydft = mydft(data,nfft)
n_mag_mydft = len(mag_mydft)
print(np.abs(mag_mydft))
print("length of signal)",len(data))
print("length of mydft\t\t:",n_mag_mydft)
allocate_mydft = timeit.timeit("'mydft(signal_rand)'",number=1)
print("Allocate Time of mydft\t:",allocate_mydft,"second")
max_mag_mydft = max(np.abs(mag_mydft)[:int(nfft/2)])
id_max_mag_mydft = np.argmax(np.abs(mag_mydft)[:int(nfft/2)])
freq_mag_mydft = freq[id_max_mag_mydft]
print("Frequency\t\t:", freq_mag_mydft,"Hz")
print("Maginutde\t\t:",max_mag_mydft)

print("\nFFT Python Library")
mag_fft = fft(data,nfft)
n_mag_fft = len(mag_fft)
print(np.abs(mag_fft))
print("Length of fft\t\t:",n_mag_fft)
allocate_fft = timeit.timeit("'scipy.fftpack.fft(signal_rand,nfft)'",number=1)
print("Allocate Time of fft\t:",allocate_fft,"second")
max_mag_fft = max(np.abs(mag_fft)[:int(nfft/2)])
id_max_mag_fft = np.argmax(np.abs(mag_fft)[:int(nfft/2)])
freq_mag_fft = freq[id_max_mag_fft]
print("Frequency\t\t:", freq_mag_mydft,"Hz")
print("Maginutde\t\t:",max_mag_fft)

# Comparing the result. If the result is True, myDFT is good
check = np.allclose(mag_mydft,mag_fft)
print("Check\t\t\t:",check)

# Plot
# Spectrum
fig1 = plt.figure(1)
subfig1 = fig1.add_subplot(211)
plt.plot(freq,np.abs(mag_mydft),color='blue',label="MyDFT")
plt.ylabel('Magnitude')
plt.title("MyDFT vs FFTpack (Python Library)")
plt.legend()
subfig2 = fig1.add_subplot(212)
plt.plot(freq,np.abs(mag_fft),color='red',label="FFTpack")
plt.ylabel('Magnitude')
plt.xlabel('Frequency(Hz)')
plt.legend()

# Signal
fig2 = plt.figure(2)
subfig3 = fig2.add_subplot(211)
plt.plot(t,signal,color='blue',label="Raw")
plt.ylabel('Amplitude')
plt.title("Random Signal")
plt.legend()
subfig4 = fig2.add_subplot(212)
plt.plot(t,data,color='red',label="Add Random")
plt.ylabel('Amplitudo')
plt.xlabel('Time(second)')
plt.legend()
plt.show()
