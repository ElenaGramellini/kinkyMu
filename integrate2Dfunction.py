import numpy as np
from scipy import integrate
import math

# Define the function f(x, y)
def f(x, y):
    return x**2 + y**2

# Define the integration limits for x and y
x_lower = 0
x_upper = 1
y_lower = 0
y_upper = 2

# Perform the double integration using dblquad()
result, error = integrate.dblquad(f, x_lower, x_upper, y_lower, y_upper)

print("Result:", result)
print("Error:", error)




# example parametric function
def flux(E, theta):
    I0 = 70.7
    E0 = 4.29 # GeV
    epsilon = 854
    n = 3.01
    Rd = 174
    D = np.sqrt(Rd*Rd*np.cos(theta) + 2*Rd + 1 ) - Rd*np.cos(theta)
    N = 46.99501630666583
    P0 = I0*N
    P1 = (E0 + E)** (-n)
    P2 = (1+E/epsilon)**(-1)
    P3 = D**(-n+1)
    x = P0*P1*P2*P3
    return x


# Define the integration limits for x and y
x_lower = 1
x_upper = 1000
y_lower = -1.*math.pi
y_upper = math.pi

# Perform the double integration using dblquad()
result, error = integrate.dblquad(f, x_lower, x_upper, y_lower, y_upper)

print("Result:", result)
print("Error:", error)

