# -*- coding: utf-8 -*-
from __future__ import division, print_function
from pylab import *
from matplotlib import animation

lambda0 = 1.55e-6
N_lambda = 20
dx = lambda0 / N_lambda
c = 2.99792458e8
S = 1
dt = S*dx/c
T = lambda0/c
xmin = 0
xmax = 20 * lambda0
nbx = int( around((xmax-xmin)/dx,0) + 1)

unp = zeros(nbx) # u a l'instant n+1
un  = zeros(nbx) # u a l'instant n
unm = zeros(nbx) # u a l'instant n-1

x = linspace(xmin, xmax, nbx)

# tableau pour les indices de refraction
indice = zeros(nbx)
for i in range(nbx):
    if x[i] > 7*lambda0 and x[i] < 12*lambda0:
        indice[i] = 1.45
    else:
        indice[i] = 1
        
eps_r = indice**2      

nbt = 800

fig = figure() # initialise la figure
line, = plot(x,un) 
xlim(xmin, xmax)
ylim(-2,2)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def animate(n):
    tnp = (n+1)*dt
    # champ de la source
    unp[0] = cos(2*pi/T*tnp)*exp(-( (tnp-3*T)/T )**2)
    # calcul du champ avec le schema numerique
    for i in range(1,nbx-1):
        unp[i] = S**2/eps_r[i] *(un[i+1]-2*un[i]+un[i-1]) + 2*un[i] - unm[i]
    line.set_data(x, unp)
    unm[:] = un[:]
    un[:] = unp[:]
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)

show()
