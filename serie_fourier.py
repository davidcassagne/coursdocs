from pylab import *

a = 1
nmax = 5
nmin = -nmax
n = range(nmin,nmax+1)
nbn = len(n)
V_K = zeros(nbn)
for i in range(nbn):
    if n[i] == 1:
        V_K[i] = 1
    if n[i] == 2:
        V_K[i] = 0.5
    if n[i] == 5:
        V_K[i] = 0.5
xmin = -3
xmax = 3
nbx = 400
x = linspace(xmin, xmax, nbx)
V = zeros(nbx)
for i in range(nbn):
    V = V + V_K[i]*exp(1j*n[i]*2*pi/a*x)
plot(x,real(V))
show()


        
