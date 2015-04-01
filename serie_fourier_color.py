from pylab import *

a = 1
nmax = 5
nmin = -nmax
n = range(nmin,nmax+1)
nbn = len(n)
V_K = zeros(nbn)*1j
for i in range(nbn):
    if n[i] == 1:
        V_K[i] = exp(1j*pi/2)
    if n[i] == 2:
        V_K[i] = 0
    if n[i] == 3:
        V_K[i] = 0
xmin = -3
xmax = 3
nbx = 400
x = linspace(xmin, xmax, nbx)
V = zeros(nbx)
for i in range(nbn):
    V = V + V_K[i]*exp(1j*n[i]*2*pi/a*x)
    
z = V

X = array([x,x])

y0 = zeros(len(x))
y = abs(z)
Y = array([y0,y])

Z = array([z,z])
C = angle(Z)

plot(x,y,'k')
ylim(0,3)

pcolormesh(X, Y, C, shading='gouraud', cmap=cm.hsv, vmin=-pi, vmax=pi)
colorbar()
    
show()
