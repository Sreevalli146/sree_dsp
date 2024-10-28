import numpy as np
def circular_convolution(x,h):
	x=np.array(x)
	h=np.array(h)
	N=len(x)
	M=len(h)
	h_padded=np.pad(h,(0,N-M))
	y=np.zeros(N)
	for n in range(N):
		for m in range(M):
			y[n]+=x[(n-m)%N]*h_padded[m]
	return y
print("OVERLAP AND SAVE METHOD")
print()	
x1=[0,0,1,2,3,1]
x2=[3,1,2,3,1,2]
x3=[1,2,3,1,2,3]
h=[1,-1,1]
y1=circular_convolution(x1,h)	
print("y1=",y1)
y2=circular_convolution(x2,h)
print("y2=",y2)
y3=circular_convolution(x3,h)
print("y3=",y2)
y1_new=[]
y2_new=[]
y3_new=[]
for i in range(2,len(y1)):
	y1_new.append(int(y1[i]))
	y2_new.append(int(y2[i]))
	y3_new.append(int(y3[i]))
print("modified values of y:")
print("y1=",y1_new)
print("y2=",y2_new)
print("y3=",y3_new)	
y=[]
for i in range(len(y3_new)):
	y.append(int(y1_new[i]))
for i in range(len(y3_new)):
	y.append(int(y2_new[i]))
for i in range(int(len(y3_new))):
	y.append(y3_new[i])		
print("y[n]=",y)	


# OVERLAP AND ADD

print("OVERLAP AND SAVE METHOD")
x4=[1,2,3,1,0,0]
x5=[2,3,1,2,0,0]
x6=[3,1,2,3,0,0]
y4=circular_convolution(x4,h)	
print("y4=",y4)
y5=circular_convolution(x5,h)
print("y5=",y5)
y6=circular_convolution(x6,h)
print("y6=",y6)
y4_new=[]
y5_new=[]
y6_new=[]
for i in range(len(y4)-2):
	y4_new.append(int(y4[i]))
	y5_new.append(int(y5[i]))
	y6_new.append(int(y6[i]))
print("modified values of y:")
print("y4=",y4_new)
print("y5=",y5_new)
print("y6=",y6_new)	
y_new=[]
for i in range(len(y4_new)):
	y_new.append(int(y4_new[i]))
for i in range(len(y5_new)):
	y_new.append(int(y5_new[i]))
for i in range(int(len(y5_new))):
	y_new.append(y6_new[i])		
print("y[n]=",y_new)
