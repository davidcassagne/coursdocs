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
xmax = 40 * lambda0
nbx = int( around((xmax-xmin)/dx,0) + 1)

unp = zeros(nbx) # u a l'instant n+1
un  = zeros(nbx) # u a l'instant n
unm = zeros(nbx) # u a l'instant n-1

x = linspace(xmin, xmax, nbx)

# tableau pour les indices de refraction
indice = ones(nbx)
indice_milieu2 = 1.45
indice_milieu1 = sqrt(indice_milieu2)
#indice_milieu1 = indice_milieu2

largeur = lambda0 / (4 * indice_milieu1)
position = (xmin + xmax)/2
for i in range(nbx):
    if abs(x[i]-position)<largeur/2:
        indice[i] = indice_milieu1
    if x[i]-position>largeur/2:
        indice[i] = indice_milieu2
      
eps_r = indice**2      

nbt = 2000

fig = figure() # initialise la figure
line, = plot(x,un) 
xlim(xmin, xmax)
ylim(-2,2)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data(x,indice)
    return line,

def animate(n):
    tnp = (n+1)*dt
    # champ de la source
    if tnp < 20*T:
        unp[0] = cos(2*pi/T*tnp)*exp(-( (tnp-10*T)/(4*T) )**2)
    else:
        unp[0] = un[1]
    # calcul du champ avec le schema numerique
    for i in range(1,nbx-1):
        unp[i] = S**2/eps_r[i] *(un[i+1]-2*un[i]+un[i-1]) + 2*un[i] - unm[i]
    unp[nbx-1] = un[nbx-2]
    line.set_data(x, unp)
    unm[:] = un[:]
    un[:] = unp[:]
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)

show()
