# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:59:45 2015

@author: cassagne
"""

from pylab import *
from matplotlib import animation

dx = 0.005

xdata = []
ydata = []

fig = figure() # initialise la figure
line = plot([],[],"r",[],[],"g")
xlim( 0, 1)
ylim(-1, 1)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line[0].set_data([0.2, 0.6],[-0.5, 0.5])
    line[1].set_data([0.2, 0.4],[-0.3, 0.5])
    return line

def animate(i): 
    x = i * dx
    y = cos(2*pi*x)
    xdata.append(x)
    ydata.append(y)
    line[0].set_data(xdata, ydata)
    return line
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=150, blit=True, interval=20, repeat=False)

show()
