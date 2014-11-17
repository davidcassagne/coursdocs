# -*- coding: utf-8 -*-
from __future__ import division
from pylab import *
from matplotlib import animation

k0 = 2*pi
w0 = 2*pi

delta_k = 0.2*k0
delta_w = 0.4*w0


k1 = k0 - delta_k / 2
k2 = k0 + delta_k / 2

w1 = w0 - delta_w / 2
w2 = w0 + delta_w / 2

xmin = 0
xmax = 10
nbx = 200

x = linspace(xmin, xmax, nbx)
y = zeros((3,nbx))
dt = 0.02

fig = figure() # initialise la figure
line = plot([],[],"b",[],[],"r",[],[],"r") 
xlim(xmin, xmax)
ylim(-2,2)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    for j in range(3):
        line[j].set_data([],[])
    return line 

def animate(i): 
    t = i * dt
    y[0] = cos(k1*x - w1*t) + cos(k2*x - w2*t)
    y[1] = 2*cos(delta_k/2 * x - delta_w/2 * t)
    y[2] = -y[1]
    for j in range(3):
        line[j].set_data(x, y[j])
    return line
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, blit=True, interval=20, repeat=False)

show()


