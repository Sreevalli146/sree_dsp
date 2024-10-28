import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,4,3,2,1]
n=len(x)
def dtft(x,n):
    w=np.arange(-np.pi,np.pi,0.01)
    X=np.zeros(len(w),dtype=complex)
    for k in range(len(w)):
        X[k]=sum(x[i]*np.exp(-1j*w[k]*i) for i in range(n))
    return w,X
w,X=dtft(x,n)
for i in range(len(X)):
    X[i]=X[len(X)-i-1]
    print(X[i])
plt.figure(figsize=(8,4))
plt.title("X1(W)")
plt.plot(w,np.abs(X))
w,Y=dtft(y,n)
plt.figure(figsize=(8,4))
plt.title("Y1(W)")
plt.plot(w,np.abs(Y),color='gold')
plt.show()
if(X.all()==Y.all()):
    print("time reversal verified")
