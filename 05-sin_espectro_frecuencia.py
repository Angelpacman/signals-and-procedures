import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

Fs = 500.0;                 # razon de muestreo
Ts = 1.0/Fs;                # intevalo de muestreo
t = np.arange(0,1,Ts)       # vector tiempo
ff = 75;                    # frecuencia de la señal
y = np.cos(2*pi*ff*t)       # señal analogica continua en el tiempo

def plotSpectrum(y,Fs):

    n = len(y)                  # longitud de la señal
    k = np.arange(n)
    T = n/Fs
    frq = k/T                   # 2 lados del rango de frecuancia
    frq = frq[range(n//2)]      # Un lado del rango de frecuencia

    Y = np.fft.fft(y)/n         # fft calcula la normalizacion
    Y = Y[range(n//2)]

    plt.plot(frq,np.abs(Y),'r') # grafica el espectro de frecuencia
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('|Y(f)|')

#Proceso de graficar la señal
plt.subplot(2,1,1)
plt.plot(t,y)
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.subplot(2,1,2)
#Se llama a la funcion con la señal y la razon de muestreo
plotSpectrum(y,Fs)
plt.grid()
plt.show()
