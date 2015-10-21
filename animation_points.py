from pylab import *
from matplotlib import animation

dx = 0.005

xdata = []
ydata = []

fig = figure() # initialise la figure
line, = plot([],[], ",") 
xlim( 0, 1)
ylim(-1, 1)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def animate(i): 
    global xdata
    global ydata
    x = i * dx
    y = cos(2*pi*x)
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=150, blit=True, interval=20, repeat=False)

show()
