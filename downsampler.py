import numpy as np
from matplotlib import pyplot as plt
signal=[1,2,3,4,5]
l=2
dsignal=signal[::l]

plt.subplot(2,1,1)
plt.stem(signal)


plt.subplot(2,1,2)
plt.stem(dsignal)

plt.show()
