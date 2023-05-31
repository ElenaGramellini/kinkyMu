import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_box_and_line(box_min, box_max, line_start, line_end):
    # Create figure and 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot box
    box_x = [box_min[0], box_max[0], box_max[0], box_min[0], box_min[0], box_max[0], box_max[0], box_min[0]]
    box_y = [box_min[1], box_min[1], box_max[1], box_max[1], box_min[1], box_min[1], box_max[1], box_max[1]]
    box_z = [box_min[2], box_min[2], box_min[2], box_min[2], box_max[2], box_max[2], box_max[2], box_max[2]]
    ax.plot(box_x, box_y, box_z, 'b-')

    # Plot line
    line_x = [line_start[0], line_end[0]]
    line_y = [line_start[1], line_end[1]]
    line_z = [line_start[2], line_end[2]]
    ax.plot(line_x, line_y, line_z, 'r-')

    # Set plot limits
    ax.set_xlim(min(box_min[0], line_start[0], line_end[0]), max(box_max[0], line_start[0], line_end[0]))
    ax.set_ylim(min(box_min[1], line_start[1], line_end[1]), max(box_max[1], line_start[1], line_end[1]))
    ax.set_zlim(min(box_min[2], line_start[2], line_end[2]), max(box_max[2], line_start[2], line_end[2]))

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()


# Example usage
box_min = [-1, -1, -1]
box_max = [1, 1, 1]
line_start = [0, 0, 0]
line_end = [1, 1, 1]

visualize_box_and_line(box_min, box_max, line_start, line_end)
