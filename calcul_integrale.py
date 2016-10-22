# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 08:48:00 2016

@author: cassagne
"""

import numpy as np
from scipy.integrate import simps

xmin = 0
xmax = 3*np.pi/2
nbx = 21
nbi = nbx - 1 # nombre d'intervalles

x = np.linspace(xmin, xmax, nbx)
y = np.cos(x)
h = x[1]-x[0]

integrale1 = 0
for i in range(nbi):
    integrale1 = integrale1 + y[i]*h
print("integrale1 =", integrale1)

integrale2 = 0
for i in range(nbi):
    integrale2 = integrale2 + (y[i]+y[i+1])*h/2
print("integrale2 =", integrale2)

integrale3 = (y[0]+y[nbx-1])*h/3
for i in range(1,nbx-1,2):
    integrale3 = integrale3 + 4*h/3*y[i]
for i in range(2,nbx-1,2):
    integrale3 = integrale3 + 2*h/3*y[i]
print("integrale3 =", integrale3)

resultat_exact = -1
err_rel1 = abs(integrale1-resultat_exact)/resultat_exact
err_rel2 = abs(integrale2-resultat_exact)/resultat_exact
err_rel3 = abs(integrale3-resultat_exact)/resultat_exact
print("erreur relative1 =", err_rel1)
print("erreur relative2 =", err_rel2)
print("erreur relative3 =", err_rel3)

integrale1sum = np.sum(y[:nbi])*h
print("integrale1sum =", integrale1sum)
integrale2sum = ( (y[0]+y[nbx-1])/2 + np.sum(y[1:nbx-1]) )*h
print("integrale2sum =", integrale2sum)
integrale2sum_b = ( np.sum(y[0:nbx-1]) + np.sum(y[1:nbx]) )*h/2
print("integrale2sum_b =", integrale2sum_b)
integrale3sum = ( y[0] + y[nbx-1] + 4*np.sum(y[1:nbx-1:2]) +
                  2*np.sum(y[2:nbx-1:2]) )*h/3
print("integrale3sum =", integrale3sum)
print("scipy.integrate.simps =", simps(y,x))
