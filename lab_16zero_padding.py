import numpy as np
from matplotlib import pyplot as plt
def dft(x):
	N=len(x)
	d=np.zeros(N,dtype=complex)
	for k in range(N):
		for n in range(N):
			d[k]+=x[n]*np.exp(-2j*np.pi*k*n/N)
	return d
def zeropadding(x,new_length):
	zero_padded=np.pad(x,(0,new_length-len(x)))
	return dft(zero_padded)
x=[1,2,3,4]	
dft_original=dft(x)
z=input("Enter number of zeros you want:")
new_length=len(x)+int(z)
dft_zero=zeropadding(x,new_length)
plt.figure(figsize=(14,8))
plt.subplot(2,2,1)
plt.stem(x)
plt.title("original")
plt.subplot(2,2,2)
plt.stem(np.abs(dft_original))
plt.title("dft of original")
plt.subplot(2,2,3)
plt.stem(np.pad(x,(0,new_length-len(x))))
plt.title("zero padded")
plt.subplot(2,2,4)
plt.stem(np.abs(dft_zero))
plt.title("dft of zero padded")
plt.show()	
