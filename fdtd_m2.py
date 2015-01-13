# -*- coding: utf-8 -*-
from pylab import *
from matplotlib import animation

c = 1
dt = 0.01
S = 0.99
dx = c * dt / S

nbx = 100
xmin = 0
xmax = xmin+dx*(nbx-1)

x = linspace(xmin, xmax, nbx)
unp = zeros(nbx)
un = zeros(nbx)
unm = zeros(nbx)

nbt = 200

fig = figure() # initialise la figure
line, = plot([],[]) 
xlim(xmin, xmax)
ylim(-1,1)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def animate(n): 
    tnp = (n+1) * dt
    if tnp>0.05 and tnp<0.15:
        unp[0] = 1
    else:
        unp[0] = 0
    for i in range(1,nbx-1):
        unp[i]=S**2 * (un[i+1]-2*un[i]+un[i-1]) + 2*un[i] - unm[i]
    line.set_data(x, unp)
    unm[:]=un[:]
    un[:]=unp[:]
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)

show()
