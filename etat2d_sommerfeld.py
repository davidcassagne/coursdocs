
from pylab import *

L = 3


xmin = 0
xmax = L
nbx = 41
ymin = 0
ymax = L
nby = 41

nx = 1
ny = 3

kx = nx * pi/L
ky = ny * pi/L


x = linspace(xmin, xmax, nbx)
y = linspace(ymin, ymax, nby)
X, Y = meshgrid(x, y)

Z = sin(kx * X) *sin(ky * Y)

imshow(Z, interpolation="bicubic", 
       origin="lower", extent=[xmin,xmax,ymin,ymax])
colorbar()

show()
