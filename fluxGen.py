#[  ] a realistic muon flux
#     [ X ] Find the paper for the flux: it's a function of (Energy, Polar Angle). Archive 1606.06907
#           The assumption is that the flux doesn't change in the azimuthal angle, and in height.  
#     [ X ] Code the Phi (Energy, Polar Angle)
#     [   ] Check it's correct against data reported in the paper
#          [   ] Find the data
#                [] Phys.Lett.B 594 (2004) 35-46
#                [] https://iopscience.iop.org/article/10.1088/0370-1328/80/3/315/pdf
#          [   ] Solve normalization issue


import numpy as np
import matplotlib.pyplot as plt
import random
import math


# example parametric function
def flux(E, theta, Ec):
    I0 = 88.0
    E0 = 4.29 # GeV
    epsilon = 854
    n = 3.09
    Rd = 174
    D = np.sqrt(Rd*Rd*np.cos(theta) + 2*Rd + 1 ) - Rd*np.cos(theta)
    N = (n - 1)*((E0 + Ec)**(n - 1))
    #N=100
    P0 = I0*N
    P1 = (E0 + E)** (-n)
    P2 = (1+E/epsilon)**(-1)
    P3 = D**(-n+1)
    x = P0*P1*P2*P3
    return x


# Generate parameter values
t_values = np.linspace(0, 10000, 10000)

# Evaluate the parametric function
y_values = flux(t_values, 0, 10000)

# Create the plot
plt.loglog(t_values, y_values)
#plt.loglog(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Parametric Function: Flux')
plt.grid(True)

# Show the plot
plt.show()
