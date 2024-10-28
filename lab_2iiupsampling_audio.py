from scipy.io import wavfile
import numpy as np
fs,x=wavfile.read('/home/mouni2005/Documents/E2S1/DSP LAB/Adver.wav')
def upsampling(xi,a):
	if a>1:
		y=np.zeros.(len(xi)*a,xi.shape[1])
		y[::a]=xi
		wavfile.read('upsamp.wav',fs,y)
a=int(input("Enter upsampling factor:"))
updsampling(x,a)
		
