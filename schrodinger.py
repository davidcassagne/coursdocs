from __future__ import division, print_function
#============================================================================
# Author:  James Nagel <nagel@mers.byu.edu>
#          5/25/07
#
# Updates by Fernando Perez <Fernando.Perez@colorado.edu>, 7/28/07
#============================================================================
#  Numerical and plotting libraries
from pylab import *
ion()

#=============================================================================
# Utility functions
#  Defines a quick Gaussian pulse function to act as an envelope to the wave
#  function.

def fillax(x, y, *args, **kw):
    """Fill the space between an array of y values and the x axis.
    All args/kwargs are passed to the pylab.fill function.
    Returns the value of the pylab.fill() call.
    """
    xx = concatenate((x,array([x[-1],x[0]],x.dtype)))
    yy = concatenate((y,zeros(2,y.dtype)))
    return fill(xx, yy, *args,**kw)

#=============================================================================
#
#  Simulation Constants.  Be sure to include decimal points on appropriate
#  variables so they become floats instead of integers.
#
#N    = 1200     #  Number of spatial points.
#T    = 5*N      #  Number of time steps.  5*N is a nice value for terminating
                #  before anything reaches the boundaries.
Tp   = 10      #  Number of time steps to increment before updating the plot.
m    = 9.1093826e-31           #  Masse de la particule (ici un electron)
hbar = 6.62606896e-34 / (2*pi) #  Constante de Planck / (2*pi) -> hbar

lambda0 = 40 # longueur d'onde de l'onde centrale du paquet
sigma = 0.9*lambda0 # parametre de largeur du paquet gaussien

dx = lambda0/40 # pas d'espace
nbx = 1200        # nombre de points d'espace
T = int(2.7*nbx)
xmin = 0
xmax = xmin+(nbx-1)*dx
x = linspace(xmin, xmax, nbx)
THCK = 15       # "Thickness" of the potential barrier (if appropriate
                # V-function is chosen)
# Uncomment the potential type you want to use here:
# Zero potential, packet propagates freely.
POTENTIAL = 'barrier'
# Potential step.  The height (V0) of the potential chosen above will determine
# the amount of reflection/transmission you'll observe
#POTENTIAL = 'step'
# Potential barrier.  Note that BOTH the potential height (V0) and thickness
# of the barrier (THCK) affect the amount of tunneling vs reflection you'll
# observe.
#POTENTIAL = 'barrier'
#  Initial wave function constants
#sigma = 50.0 # Standard deviation on the Gaussian envelope (remember Heisenberg
             #  uncertainty).
k0 = 2*pi/lambda0
x0 = (xmin+xmax)/2.0 - 4*sigma # centre
# k0 = pi/20 # Wavenumber (note that energy is a function of k)
# Energy for a localized gaussian wavepacket interacting with a localized
# potential (so the interaction term can be neglected by computing the energy
# integral over a region where V=0)
E = hbar**2/(2.0*m) * (k0**2+0.5/sigma**2) # Energie moyenne du paquet d'ondes
V0 = 2*E
V = zeros(nbx)
V[nbx/2:nbx/2+THCK] = V0

#  More simulation parameters.  The maximum stable time step is a function of
#  the potential, V.
Vmax = V.max()            #  Maximum potential of the domain.
dt   = hbar/(2*hbar**2/(m*dx**2)+Vmax)         #  Critical time step.
c1   = hbar*dt/(m*dx**2)                       #  Constant coefficient 1.
c2   = 2*dt/hbar                               #  Constant coefficient 2.
c2V  = c2*V  # pre-compute outside of update loop
# Print summary info
print('One-dimensional Schrodinger equation - time evolution')
print 'Wavepacket energy:   ',E
print 'Potential height V0: ',V0
print 'Barrier thickness:   ',THCK


psiR = zeros(nbx) #  Partie reelle a l'instant n
psiI = zeros(nbx) #  Partie imaginaire 

# paquet d'ondes au depart
# cas d'un paquet d'ondes gaussien de vecteur d'onde k0 
psiR = cos(k0*x)*exp(-(x-x0)**2 / (2*sigma**2))
psiI = sin(k0*x)*exp(-(x-x0)**2 / (2*sigma**2))
# Calcul de la densite de probabilite
psi2 = psiR**2 + psiI**2
#  Normalize the wave functions so that the total probability in the simulation
#  is equal to 1.
P   = dx * psi2.sum()                      #  Total probability.
nrm = sqrt(P)
psiR = psiR / nrm
psiI = psiI / nrm
psi2 = psi2 / P
#  Initialize the figure and axes.
figure()
ymax = 1.5*psiR.max()
axis([xmin,xmax,-ymax,ymax])
#  Initialize the plots with their own line objects.  The figures plot MUCH
#  faster if you simply update the lines as opposed to redrawing the entire
#  figure.  For reference, include the potential function as well.
lineR, = plot(x, psiR, 'b', label='Real')
lineI, = plot(x, psiI, 'r', label='Imag')
lineP, = plot(x, 6 * psi2, 'k', label='Prob')
# For non-zero potentials, plot them and shade the classically forbidden region
# in light red, as well as drawing a green line at the wavepacket's total
# energy, in the same units the potential is being plotted.
if Vmax !=0 :
    # Scaling factor for energies, so they fit in the same plot as the
    # wavefunctions
    Efac = ymax/2.0/Vmax
    V_plot = V*Efac
    plot(x, V_plot,':k', zorder=0)   #  Potential line.
    fillax(x, V_plot, facecolor='y', alpha=0.2,zorder=0)
    # Plot the wavefunction energy, in the same scale as the potential
    axhline(E*Efac, color='g', label='Energy',zorder=1)
legend(loc='lower right')
draw()
# I think there's a problem with pylab, because it resets the xlim after
# plotting the E line.  Fix it back manually.
xlim(xmin,xmax)

for t in range(T+1):
    #  Apply the update equations.
    for i in range(1,nbx-1): 
        psiI[i] = psiI[i] + c1*(psiR[i+1]-2*psiR[i]+psiR[i-1]) - c2V[i]*psiR[i]
    for i in range(1,nbx-1): 
        psiR[i] = psiR[i] - c1*(psiI[i+1]-2*psiI[i]+psiI[i-1]) + c2V[i]*psiI[i]
                          
    #  Only plot after a few iterations to make the simulation run faster.
    if t % Tp == 0:
        #  Compute observable probability for the plot.
        psi2 = psiR**2 + psiI**2
        # Update the plots.
        lineR.set_ydata(psiR)
        lineI.set_ydata(psiI)
        # Note: we plot the probability density amplified by a factor so it's a
        # bit easier to see.
        lineP.set_ydata(6*psi2)
        pause(0.01)
        draw()
ioff()
show()
