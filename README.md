# Recursive FFT
In previous repository [pyDFT](https://github.com/auliakhalqillah/pyDFT), I had described the simple numerical of Discrete Fourier Transform (DFT). Now, in this repository, I try to describe the Fast Fourier Transform (FFT) by using even and odd part which is applied with recursion method. The function of FFT in this repository is called `mydft`. The `mydft` has been compared with `scipy.fftpack` which is from python library.
# Recursion Method
The short brief of recursion method is, a function call the itself inside function itself. You can get the basic illustration on [Iteration and Recursion Function in Python](https://sharing.auliakhalqillah.com/2020/04/11/iteration-and-recursion-function-in-python/). 
# Usage
The FFT program in this repository has a function like
```
spectrum = mydft(data)
```
or if you want to input certain number, e.g. nfft = 1024, you can type the function;
```
spectrum = mydft(data,nfft)
```
### Note
The function of `mydft` will process the data if the number of data is power of two. But, if you input the number of data is not power of two, the function will automatic increase/decrease the number of data based on power of two. 
For an example, if number input data is 5000. This 5000 is not power of two, but a value of power of two that close to 5000 is 2^12 = 4096. Its means, the 5000 will be decreased to 4096. 

Another case, if the nfft value is set in function `'mydft`, but the number of data is less than to nfft, the rest of nfft value will be padded to number of data.
# Contact
Email: auliakhalqillah.mail@gmail.com
# Sources
1. [Paul Heckbert (1998) Fourier Transforms and the Fast Fourier Transform (FFT) Algorithm](http://www.cs.cmu.edu/afs/andrew/scs/cs/15-463/2001/pub/www/notes/fourier/fourier.pdf)
2. [Michael T. Heideman, Don H. Johnson, C. Sidney Burrus (1984),Gauss and the history of the fast Fourier transform](http://www.cis.rit.edu/class/simg716/Gauss_History_FFT.pdf)
3. [Amente Bekele (2016),Cooley-Tukey Algorithms](http://people.scs.carleton.ca/~maheshwa/courses/5703COMP/16Fall/FFT_Report.pdf)
4. [Jake VanderPlas (2013), Understanding the FFT algorithm](https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/)
5. [Sho Nakagome (2019), Fourier Transform 101 – Part 5: Fast Fourier Transform (FFT)](https://medium.com/sho-jp/fourier-transform-101-part-5-fast-fourier-transform-fft-38c22e05ead3)
