"""import numpy as np
from matplotlib import pyplot as plt

def circular_convolution(x,h):
	N=6
	y=np.zeros(N)
	for n in range(N):
		#y[n]=sum(x*h_padded[(n-k%N)] for k in range(N))
		for k in range(N):
			p=n-k%N
			y[n]=x*h[p]
	return y	
xx=[1,2,3,1,2,3,1,2,3,1,2,3]
hh=[1,-1,1]
L=len(xx)
M=len(hh)
length=L+M-1
x1=[0,0,1,2,3,1]
x2=[3,1,2,3,1,2]
x3=[1,2,3,1,2,3]
h_padded=np.pad(hh,(0,len(x1)-len(hh)))
print(h_padded)
y1=circular_convolution(x1,h_padded)
y2=circular_convolution(x2,h_padded)
y3=circular_convolution(x3,h_padded)
print("y1=",y1)
print()
print("y2=",y2)
print()
print("y3=",y3)
print()"""

import numpy as np

# Define the sequences
x = np.array([0, 0, 1, 2, 3, 1])
h = np.array([1, -1, 1])

# Get the length of x and h
N = len(x)
M = len(h)

# Extend h to the length of x by zero-padding
h_padded = np.pad(h, (0, N - M), mode='constant')

# Initialize the result array
y = np.zeros(N)

# Perform circular convolution
for n in range(N):
    for m in range(M):
        y[n] += x[n - m] * h_padded[m]

# Output the result
print("Circular Convolution Result:", y.astype(int))

