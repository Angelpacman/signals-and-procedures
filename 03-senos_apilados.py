import numpy as np
import matplotlib.pyplot as plt

f = 1/(2*np.pi)
t = np.linspace(0,2*np.pi,200) #two cycles, 100 points each
y1 = (4/np.pi)*np.sin(2*np.pi*f*t)
y3 = y1 + (4/(3*np.pi))*np.sin(2*np.pi*3*f*t)
y5 = y3 + (4/(5*np.pi))*np.sin(2*np.pi*5*f*t)
sqwave = np.sign(np.sin(2*np.pi*f*t)) #an actual square wave
plt.plot(t,y1, t,y3, t,y5, t, sqwave)

sq = np.zeros(len(t))
#print(len(sq)) #preallocate the output array
for h in np.arange(1,10,2):
    sq += (4/(np.pi*h))*np.sin(2*np.pi*f*h*t)

plt.plot(t,sq,t,sqwave)
plt.grid()
plt.show()


Fourier = np.fft.fft(sq)
fig, ax = plt.subplots()
ax.plot(t[:100], f/2.0 * np.abs(Fourier[:100]))
print('tamaño de Fourier es:' +str(len(Fourier)))
print('tamaño de t es:' +str(len(t)))
plt.grid()
plt.show()
