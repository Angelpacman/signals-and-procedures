import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,4,64);
f = np.exp(-0.5*t)*np.sin(2*np.pi*t)
plt.subplot(2,1,1)
plt.plot(t,f)
plt.title('formas digital & analogica')
plt.xlabel('señal digital')
plt.ylabel('f(k)')
plt.subplot(2,1,2)
markerline, stemlines, baseline = plt.stem(t,f,'-.') #plt.stem(np.ndarray(t(1,3,128)),np.arange(f(1,4,128),'-.'))
plt.setp(baseline, color='r', linewidth=2)
plt.show()
