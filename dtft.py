import numpy as np 
from matplotlib import pyplot as plt
x=np.array([1,2,3,4])
l=4
n=np.arange(l)
omega=np.linspace(-np.pi,np.pi)
x=np.array([sum(x[n]*np.exp(-1j*w*n)
for n in range(l))for w in omega])

plt.subplot(2,1,1)
plt.plot(omega,np.abs(x))
plt.title("Magnitude of dtft")
plt.xlabel("Frequency(rad/sample)")
plt.ylabel("Magnitude")

plt.subplot(2,1,2)
plt.plot(omega,np.angle(x))
plt.title("phase of dtft")
plt.xlabel("Frequency(rad/sample)")
plt.ylabel("Phase")

plt.show()
