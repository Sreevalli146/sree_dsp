import numpy as np
from matplotlib import pyplot as plt

x=[]
n=int(input("Enter Number"))
for i in range(0,n):
	a=int(input("Enter values"))
	x.append(a)
	
L=len(x)
N=L
print(L)
omega=np.arange(-np.pi,np.pi,0.001*np.pi)
w1=[]
def DFT(x,N):
	for k in range(0,N):
		s=0
		for i in range(0,N):
			s=s+(x[i]*np.exp((-1j*2*np.pi*k*i)/N))
		w1.append(s)
	return w1
	
k=np.arange(0,N)
X=DFT(x,N)
print(w1)
w2=[]
for i in range(0,4):
	w2.append(np.abs(w1[i]))
	
print(w2)
plt.subplot(2,1,1)
plt.stem(k,w2)

plt.subplot(2,1,2)
plt.stem(k,np.angle(w1))

plt.show()
