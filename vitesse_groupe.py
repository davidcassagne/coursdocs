# -*- coding: utf-8 -*-
from pylab import *
from matplotlib import animation

k0 = 2*pi
w0 = 2*pi
k1 = k0
k2 = k0+1
w1 = w0
w2 = w0+2
dt = 0.01

xmin = 0
xmax = 10
nbx = 500

x = linspace(xmin, xmax, nbx)

fig = figure() # initialise la figure
line = plot([],[],[],[],[],[]) 
xlim(xmin, xmax)
ylim(-2,2)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line[0].set_data([],[])
    line[1].set_data([],[])
    line[2].set_data([],[])
    return line

def animate(i): 
    t = i * dt
    y1 = cos(k1*x - w1*t)
    y2 = cos(k2*x - w2*t)
    line[0].set_data(x, y1)
    line[1].set_data(x, y2)
    line[2].set_data(x, y1+y2)
    return line
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=500, blit=True, interval=20, repeat=False)

show()
