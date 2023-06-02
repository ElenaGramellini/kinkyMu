import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Generate some sample data
t = np.linspace(0, 2*np.pi, 100)
x = np.sin(t)
y = np.cos(t)
z = t

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the line plot
line, = ax.plot(x, y, z)

# Animation update function
def update(frame):
    # Rotate the plot
    ax.view_init(elev=30, azim=frame)
    line.set_data(x, y)
    line.set_3d_properties(z)

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=100)
animation.save('rotation.gif', writer='pillow')
# Show the plot
plt.show()
