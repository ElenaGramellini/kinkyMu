import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the plane's parameters
point_on_plane = np.array([0, 1, 0])
normal_vector = np.array([1, 0, 0])

# Create a meshgrid for plotting
x_range = np.linspace(-5, 5, 50)
y_range = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_range, y_range)

# Calculate the corresponding z values using the plane equation
Z = (-normal_vector[0] * X - normal_vector[1] * Y - normal_vector[2] * point_on_plane[2] + 
     np.dot(normal_vector, point_on_plane)) / normal_vector[2]

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5)

# Plot the point on the plane
ax.scatter(point_on_plane[0], point_on_plane[1], point_on_plane[2], color='red', marker='o')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Visualization of a Plane')

plt.show()


