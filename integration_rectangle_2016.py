# integration numerique par la methode des rectangles avec alpha = a

import numpy as np
import matplotlib.pyplot as plt

xmin = 0
xmax = 3*np.pi/2
nbx = 20
nbi = nbx - 1 # nombre d'intervalles

x = np.linspace(xmin, xmax, nbx)
y = np.cos(x)
plt.plot(x,y,"bo-")

integrale = 0
for i in range(nbi):
    integrale = integrale + y[i]*(x[i+1]-x[i])
    # dessin du rectangle
    x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]] # abscisses des sommets
    y_rect = [0   , y[i], y[i]  , 0     , 0   ] # ordonnees des sommets
    plt.plot(x_rect, y_rect,"r")
print("integrale =", integrale)

plt.show()
