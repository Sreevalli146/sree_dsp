import numpy as np
from matplotlib import pyplot as plt

x1=np.array([1,2,3,4])
x2=np.array([4,3,2,1])
x3=x1+x2

omega=np.arange(-np.pi,np.pi,0.001*np.pi)

def dtft(x,omega):
	N=len(x)
	w=0
	for i in range(N):
		w+=x[i]*np.exp(-1j*omega*i)
	return w
w1=dtft(x1,omega)
w2=dtft(x2,omega)
w3=dtft(x3,omega)

check=w1+w2
if((w1+w2).all()==w3.all()):
	print("Linearity Verified")

plt.subplot(2,1,1)
plt.plot(omega,np.abs(check))


plt.subplot(2,1,2)
plt.plot(omega,np.abs(w3))

plt.show()

