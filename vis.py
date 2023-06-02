import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

class Display:
    def __init__(self):
        # Create a figure and a 3D axis
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def plot_line(self, tupla):
        # Plot the line
        line_start = tupla[0]
        line_end   = tupla[1]
        self.ax.plot([line_start[0], line_end[0]], [line_start[1], line_end[1]], [line_start[2], line_end[2]], 'r-', label='Line')
        self.ax.plot([line_start[0], line_end[0]], [line_start[1], line_end[1]], [line_start[2], line_end[2]], 'r-', label='Line')

    def plot_box(self, box_center, box_dimensions):
        # Plot the box
        box_x = np.array([box_center[0] - box_dimensions[0]/2, box_center[0] + box_dimensions[0]/2])
        box_y = np.array([box_center[1] - box_dimensions[1]/2, box_center[1] + box_dimensions[1]/2])
        box_z = np.array([box_center[2] - box_dimensions[2]/2, box_center[2] + box_dimensions[2]/2])        
        box_L = np.array([  box_dimensions[0]/2,   box_dimensions[0]/2])
        box_R = np.array([- box_dimensions[0]/2, - box_dimensions[0]/2])
        box_F = np.array([  box_dimensions[1]/2,   box_dimensions[1]/2])
        box_B = np.array([- box_dimensions[1]/2, - box_dimensions[1]/2])
        box_Up   = np.array([  box_dimensions[2]/2,   box_dimensions[2]/2])
        box_Down = np.array([- box_dimensions[2]/2, - box_dimensions[2]/2])

        X, Y = np.meshgrid(box_x, box_y)
        Z = np.ones_like(X) * box_Up
        self.ax.plot_surface(X, Y, Z, alpha=0.2, color='b', edgecolor='black', label='Box')
        Z = np.ones_like(X) * box_Down
        self.ax.plot_surface(X, Y, Z, alpha=0.2, color='b', edgecolor='black', label='Box')

        X, Z = np.meshgrid(box_x, box_z)
        Y = np.ones_like(X) * box_F
        self.ax.plot_surface(X, Y, Z, alpha=0.2, color='b', edgecolor='black', label='Box')
        Y = np.ones_like(X) * box_B
        self.ax.plot_surface(X, Y, Z, alpha=0.2, color='b', edgecolor='black', label='Box')

        Y, Z = np.meshgrid(box_y, box_z)
        X = np.ones_like(X) * box_L
        self.ax.plot_surface(X, Y, Z, alpha=0.2, color='b', edgecolor='black', label='Box')
        X = np.ones_like(X) * box_R
        self.ax.plot_surface(X, Y, Z, alpha=0.2, color='b', edgecolor='black', label='Box')
        

    def set_limits(self, low, up):
        # Set plot limits
        print(low)
        self.ax.set_xlim(low[0],up[0])
        self.ax.set_ylim(low[1],up[1])
        self.ax.set_zlim(low[2],up[2])

    def set_labels(self, xlabel, ylabel, zlabel):
        # Set labels
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_zlabel(zlabel)

    def set_title(self, title):
        # Set title
        self.ax.set_title(title)

    def show(self):
        # Add a legend
        #self.ax.legend()
        # Show the plot
        plt.show()


'''
# Example usage
display = Display()
display.plot_line([1, 1, 1], [5, 5, 5]) # beginning and end of line
display.plot_box([0, 0, 0], [7, 6, 7])  # center box and dimensions
display.set_limits((0, 10), (0, 10), (0, 10)) 
display.set_labels('X', 'Y', 'Z')
display.set_title('Line and Box in 3D')
display.show()
'''
