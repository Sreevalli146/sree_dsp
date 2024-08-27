import numpy as np
from matplotlib import pyplot as plt
x=[1,2,3,0,0,0]
n=len(x)

w=np.arange(-np.pi,np.pi,0.001*np.pi)
def dtft(x,omega):
	N=len(x)
	w=0
	for i in range(N):
		w+=x[i]*np.exp(-1j*omega*i)
	return w	
X_W=dtft(x,w)
X_shift_W=X_W*np.exp(-1j*w*3)

x_shift=np.roll(x,3)
x_w=dtft(x_shift,w)


if(x_w.all()==X_shift_W.all()):
	print("Time shifting property verified")
	


plt.subplot(2,1,1)
plt.plot(np.abs(x_w))

plt.subplot(2,1,2)
plt.plot(np.abs(X_W))

plt.show()
	
