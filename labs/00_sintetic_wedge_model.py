import matplotlib.pyplot as plt
import numpy as np

length, depth = 40, 100
model = 1 + np.tri(depth, length, -depth//3, dtype=int)
model[:depth//3,:] = 0

plt.imshow(model, cmap='viridis', aspect=0.2)
plt.show()

rocks = np.array([[2700, 2750],  # Vp, rho
                  [2400, 2450],
                  [2800, 3000]])
earth = rocks[model]



imp = np.apply_along_axis(np.product, -1, earth)

a = np.array([1,1,1,2,2,2,3,3,3])
b = a[1:] - a[:-1]


rc =  (imp[1:,:] - imp[:-1,:]) / (imp[1:,:] + imp[:-1,:])

plt.imshow(rc, cmap='Greys', aspect=0.2)
plt.show()


import bruges

w = bruges.filters.ricker(duration=0.100, dt=0.001, f=40)

plt.plot(w)
plt.show()
synth = np.apply_along_axis(lambda t: np.convolve(t, w, mode='same'),
                            axis=0,
                            arr=rc)

plt.imshow(synth, cmap="Greys", aspect=0.2)
plt.show()
