import numpy as np
#from numpy import fft
import matplotlib.pyplot as plt

#a continuacion se genera una se�al f que se compone de la suma de
#senoidales de las sihuientes frecuencias: 5, 12.5, 20 y 35 hz,
#dada por x(t) = 0.25+sen(2pi5t)+ sen(2pi12.5t)*sen(2pi20t)+sen(2pi35t);

N=256
T=1.0/128.0

#for i in range(N-1):
#    k=[i]
k=np.arange(N)
#print(k)
#print(len(k))

time = k*T
f0= 0.25 + 2*np.sin(2*np.pi*5+k+T) + 1*np.sin(2*np.pi*12.5*k*T)
f = f0+1.5*np.sin(2*np.pi*20*k*T) + 0.5*np.sin(2*np.pi*35*k*T)
plt.plot(time,f)

F=np.fft.fft(f)
#ff=np.linspace(0.0, 1-(1/int(len(k))),float(1.0/len(k)))
ff=np.linspace(0.0,1.0/(2.0*T), N/2)
freq=np.dot(1/T,ff)


fig, ax = plt.subplots()
ax.plot(ff, 2.0/N * np.abs(F[:N//2]))
#print(len(ff))
#print(len(F))
#plt.plot(F,freq)
#dex = np.abs(F[:N//2])
#print(dex)
plt.show()

#C = F[:N//2]
#print(C)encontre este, pero solo es para precipitacion, y ya mejor decidi programarlas https://www.youtube.com/watch?v=dfTxLNlOYK4
#ibm plex mono
