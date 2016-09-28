import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 10 # nombre de particules
nbt = 5000
xmax = 100
xmin = -xmax

x = np.zeros(n) # position initiale des particules
y = np.zeros(n)

fig = plt.figure() # initialise la figure
line, = plt.plot(x,y,"bo") 
plt.xlim(xmin, xmax)
plt.ylim(-1,1)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def animate(i): 
    global x
    x += np.sign(np.random.random(n)-0.5)
    line.set_data(x,y)
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)

plt.show()
