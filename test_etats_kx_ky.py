from pylab import *

xmin = 0
xmax = 3
nbx = 51
ymin = 0
ymax = 3
nby = 51

Kx = 2*pi/xmax
Ky = 2*pi/ymax

x = linspace(xmin, xmax, nbx)
y = linspace(ymin, ymax, nby)
X, Y = meshgrid(x, y)

Z = real(exp(1j*(1*Kx*X+0*Ky*Y))) # calcul du tableau des valeurs de Z

imshow(Z, interpolation='bicubic', origin='lower', extent=[xmin,xmax,ymin,ymax])
colorbar()

show()
