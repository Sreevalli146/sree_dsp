import numpy as np
import matplotlib.pyplot as plt
duration=0.5
sampling_rate=8000
frequency=200
num_samples=int(duration*sampling_rate)
t=np.arange(0,duration,1/sampling_rate)
sin_wave=np.sin(2*np.pi*frequency*t)
plt.plot(t,sin_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
