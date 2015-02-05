# -*- coding: utf-8 -*-
from pylab import *
from matplotlib import animation

c = 2.99792458e8
lambda0 = 1.55e-6
N_lambda = 40
dx =lambda0/N_lambda
S = 1
dt = dx*S/c
T = lambda0/c

xmin = 0
xmax = 15*lambda0
nbx = int(around((xmax-xmin)/dx,0))+1
x = linspace(xmin, xmax, nbx)
unp = zeros(nbx)
un = zeros(nbx)
unm = zeros(nbx)

indice = zeros(nbx)
indice_milieu = 2
largeur = lambda0/(2*indice_milieu)
x0 = (xmin+xmax)/2
for i in range(nbx):
    if abs(x[i]-x0)<largeur/2:
        indice[i] = indice_milieu
    else:
        indice[i] = 1

eps_r = indice**2

nbt = 2000

fig = figure() # initialise la figure
line, = plot([],[]) 
xlim(xmin, xmax)
ylim(-2,3)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data(x,indice)
    return line,

def animate(n): 
    tnp = (n+1) * dt
    if tnp<10*T:
        unp[0] = cos(2*pi*tnp/T)*exp(-((tnp- 5*T)/(2*T))**2)
    else:
        unp[0] = un[1]
    for i in range(1,nbx-1):
        unp[i]=S**2/eps_r[i] * (un[i+1]-2*un[i]+un[i-1]) + 2*un[i] - unm[i]
    unp[nbx-1] = un[nbx-2]
    line.set_data(x, unp)
    unm[:]=un[:]
    un[:]=unp[:]
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)

show()
