import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-15,15,200)

y = np.sinc(x)

Fourier = np.fft.fft(y)
fig, ax = plt.subplots()
ax.plot(x, y/2.0 * np.abs(Fourier))
plt.show()
plt.plot(x,y)
plt.grid()
plt.show()
