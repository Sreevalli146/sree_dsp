
from scipy.io import wavfile

fs, x = wavfile.read('/home/mouni2005/Documents/E2S1/DSP LAB/Adver.wav')


def sampling(x, a):
    if a > 1:
        y=x[::a]
        wavfile.write('ds1.wav',fs,y)


a=int(input("Enter sampling factor:"))
downsampling(x, a)
