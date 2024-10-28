import numpy as np
from matplotlib import pyplot as plt
def fft(x):
	N=len(x)	
	if N<=1:
		return x
	else:
		xe=fft(x[::2])
		xo=fft(x[1::2])
		X=np.zeros(N,dtype=complex)
		for k in range(N//2):
			w=np.exp((-1j*2*np.pi*k)/N)*xo[k]
			X[k]=xe[k]+w	
			X[k+N//2]=xe[k]-w
	return X
x=[1,2,-1,3]
X=fft(x)
print("FFT of x is:",X)			
		
