#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importa  coseno, linspace y pi
from numpy import cos, linspace, pi
#Importa plot, show, title, xlabel, ylabel y subplot para graficar
from pylab import plot, show, title, xlabel, ylabel, subplot, grid
#Importa fft y arange
from scipy import fft, arange

def plotSpectrum(y,Fs):
 """
 grafica la amplitud del espectro de y(t)

 """
 n = len(y) # longitud de la señal
 k = arange(n)
 T = n/Fs
 frq = k/T # 2 lados del rango de frecuancia
 frq = frq[range(n//2)] # Un lado del rango de frecuencia

 Y = fft(y)/n # fft calcula la normalizacion
 Y = Y[range(n//2)]

 plot(frq,abs(Y),'r') # grafica el espectro de frecuencia
 xlabel('Frecuencia (Hz)')
 ylabel('|Y(f)|')


if __name__ == '__main__':

    Fs = 500.0;  # razon de muestreo
    Ts = 1.0/Fs; # intevalo de muestreo
    t = arange(0,1,Ts) # vector tiempo
    ff = 75;   # frecuencia de la señal
    y = cos(2*pi*ff*t)


    #Proceso de graficar la señal
    subplot(2,1,1)
    plot(t,y)
    xlabel('Tiempo')
    ylabel('Amplitud')
    subplot(2,1,2)
    #Se llama a la funcion con la señal y la razon de muestreo
    plotSpectrum(y,Fs)
    #grid()
    show()
