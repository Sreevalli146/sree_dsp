import numpy as np
import matplotlib.pyplot as plt
duration=0.5
sampling_rate=8000
frequency=200
num_samples=int(duration*sampling_rate)
t=np.arange(0,duration,1/sampling_rate)
sin_wave=np.sin(2*np.pi*frequency*t)


new_sampling_rate=1000
new_num_samples=int(duration*new_sampling_rate)
t1=np.arange(0,duration,1/new_sampling_rate)
sin_wave2=np.sin(2*np.pi*frequency*t1)

plt.subplot(2,1,1)
plt.plot(t,sin_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("Sine wave with sampling rate of 8kHz")

plt.subplot(2,1,2)
plt.plot(t1,sin_wave2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("Sine wave with sampling rate of 1kHz")
plt.show()

