# -*- coding: utf-8 -*-
from pylab import *
from matplotlib import animation

nbx = 100
unp = zeros(nbx) # u a l'instant n+1
un  = zeros(nbx) # u a l'instant n
unm = zeros(nbx) # u a l'instant n-1

S = 0.9
c = 1
dt = 0.1
dx = c*dt / S
xmin = 0
xmax = xmin + dx*(nbx-1) 
x = linspace(xmin, xmax, nbx)

nbt = 500

fig = figure() # initialise la figure
line, = plot(x,un) 
xlim(xmin, xmax)
ylim(-2,2)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

# parametres de la source gaussienne
t0 = 30 * dt
delta = 10 * dt

def animate(n):
    tnp = (n+1)*dt
    # champ de la source
    unp[0] = exp(-( (tnp-t0)/delta )**2)
    # calcul du champ avec le schema numerique
    for i in range(1,nbx-1):
        unp[i] = S**2 *(un[i+1]-2*un[i]+un[i-1]) + 2*un[i] - unm[i]
    line.set_data(x, unp)
    unm[:] = un[:]
    un[:] = unp[:]
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)

show()
