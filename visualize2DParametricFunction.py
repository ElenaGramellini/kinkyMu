import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
# example parametric function
def flux(E, theta):
    I0 = 70.7
    E0 = 4.29 # GeV
    epsilon = 854
    n = 3.01
    Rd = 174
    D = np.sqrt(Rd*Rd*np.cos(theta) + 2*Rd + 1 ) - Rd*np.cos(theta)
    #N = 1/( (n - 1)*((E0 + Ec)**(n - 1)))
    N=46.99501630666583
    P0 = I0*N
    P1 = (E0 + E)** (-n)
    P2 = (1+E/epsilon)**(-1)
    P3 = D**(-n+1)
    x = P0*P1*P2*P3
    return x


# Define the parameter ranges
u = np.linspace(0, 10000   , 100)
v = np.linspace(0, np.pi/2., 100)

# Create a meshgrid for u and v
U, V = np.meshgrid(u, v)

# Define the parametric functions for x, y, and z
x = U
y = V
z = flux(U,V)  # Adjust this according to your function

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Parametric Surface')
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameter range
t = np.linspace(0, 2*np.pi, 100)  # Parameter values from 0 to 2*pi

# Define the parametric 2D function for x and y
x = np.cos(t)
y = np.sin(t)

# Define a function for the mapping to the third dimension
def z_function(x, y):
    return x**2 + y**2  # Adjust this mapping function as needed

z = z_function(x, y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Parametric 2D Function in 3D')
plt.show()
'''


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameter ranges
u = np.linspace(0.1, 10, 100)
v = np.linspace(0, np.pi, 100)

# Create a meshgrid for u and v
U, V = np.meshgrid(u, v)

# Define the parametric functions for x, y, and z
x = np.log(U)
y = np.sin(V)
z = U**2 + V**2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlabel('Log X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Parametric Surface with Log X-axis')
ax.set_xscale('log')  # Set logarithmic X-axis
plt.show()
