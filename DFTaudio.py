import numpy as np
import matplotlib.pyplot as plt
import librosa as lb

f,x=lb.load("/home/rguktvalley/Downloads/f2.wav")
fs=900
x=f[::int(0.5*fs)]
N=len(x)

f=[]
k1=np.arange(0,N)
omega=np.arange(0,2*np.pi,(2*np.pi/len(x)))

w1=[]

def DFT(x,N):
	for k in range(0,1800):
		s=0
		for i in range(0,1800):
			s=s+((x[i]*np.exp((-1j*2*np.pi*k*i)/N)))
		w1.append(s)
k=np.arange(0,1800)
X=DFT(x,1800)

plt.subplot(2,1,1)
plt.stem(k,np.abs(w1))
plt.show()
