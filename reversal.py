import numpy as np 
from matplotlib import pyplot as plt

x=np.array([1,2,3,4])
n=len(x)

omega=np.arange(-np.pi,np.pi,0.001*np.pi)

def dtft(x,omega):
	X=0
	for k in range(len(omega)):
		X[k]=np.sum(x*np.exp(-1j*omega[k]*np.arange(len(x))))
	return X
	
X_W=dtft(x,omega)

x_reversed=x[::-1]
X_reversed_W=dtft(x_reversed,omega)

if(X_W.all()==X_reversed_W.all()):
	print("Time reversal")

