import numpy as np
import matplotlib.pyplot as plt
from utilities import DetectorBox
from utilities import CosmicRay
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

'''

# Example usage
pDUNEBox = DetectorBox(0, 0, 0,  7.2,  7.0,  6.1) #pDUNE dimensions
novaBox  = DetectorBox(0, 0, 0, 15.6, 15.6, 78.0) #NoVA  dimensions
x_coords, y_coords, z_coords = novaBox.get_corner_points()

print("X coordinates:", x_coords)
print("Y coordinates:", y_coords)
print("Z coordinates:", z_coords)

# Example usage
eg = CosmicRay(2, 1, 2, 3, 1.2, 1.0)  # in rad
equations = eg.line_equation()
for equation in equations:
    print(equation)


    
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
'''

############# This is wrong
energy = random.uniform(0, 10)
x = random.uniform(0, 7.2)
y = random.uniform(0, 6.1)
z = 7.0
theta = random.uniform(0,   math.pi/2.)
phi   = random.uniform(0, 2*math.pi  )

ray = CosmicRay(10, 1.5, -2.0, 3.7, 45, 60)
ray.display_info()
