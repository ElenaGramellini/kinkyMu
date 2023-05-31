import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def check_intersection_line_square(line_start, line_end, square_center, square_side_length):
    # Define square vertices
    square_vertices = np.array([
        [-square_side_length / 2, -square_side_length / 2, 0],
        [-square_side_length / 2, square_side_length / 2, 0],
        [square_side_length / 2, square_side_length / 2, 0],
        [square_side_length / 2, -square_side_length / 2, 0]
    ])

    # Define square edges
    square_edges = np.array([
        [square_vertices[0], square_vertices[1]],
        [square_vertices[1], square_vertices[2]],
        [square_vertices[2], square_vertices[3]],
        [square_vertices[3], square_vertices[0]]
    ])

    # Define line direction
    line_direction = line_end - line_start

    # Check intersection between line and each square edge
    intersection_points = []
    for edge in square_edges:
        edge_start, edge_end = edge

        # Calculate intersection point between line and edge
        if np.dot(line_direction, np.cross(line_direction, edge_start - edge_end)) :
             t = np.dot(edge_start - line_start, np.cross(line_direction, edge_start - edge_end)) / np.dot(line_direction, np.cross(line_direction, edge_start - edge_end))
             intersection_point = line_start + t * line_direction

             # Check if intersection point is within the square
             if np.all(np.greater_equal(intersection_point, square_vertices.min(axis=0))) and np.all(np.less_equal(intersection_point, square_vertices.max(axis=0))):
                 intersection_points.append(intersection_point)

        return intersection_points


# Example usage
line_start = np.array([0, 0, 0])
line_end = np.array([1, 1, 1])
square_center = np.array([0, 0, 0])
square_side_length = 2

# Check intersection between line and square
intersection_points = check_intersection_line_square(line_start, line_end, square_center, square_side_length)

# Visualize the square and line
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot square
square_vertices = np.array([
    [-square_side_length / 2, -square_side_length / 2, 0],
    [-square_side_length / 2, square_side_length / 2, 0],
    [square_side_length / 2, square_side_length / 2, 0],
    [square_side_length / 2, -square_side_length / 2, 0]
])
square_edges = np.array([
    [square_vertices[0], square_vertices[1]],
    [square_vertices[1], square_vertices[2]],
    [square_vertices[2], square_vertices[3]],
    [square_vertices[3], square_vertices[0]]
])
for edge in square_edges:
    edge_x = [edge[0][0], edge[1][0]]
    edge_y = [edge[0][1], edge[1][1]]
    edge_z = [edge[0][2], edge[1][2]]
    ax.plot(edge_x, edge_y, edge_z, 'b-')

# Plot line
line_x = [line_start[0], line_end[0]]
line_y = [line_start[1], line_end[1]]
line_z = [line_start[2], line_end[2]]
ax.plot(line_x, line_y, line_z, 'r-')

# Plot intersection points
intersection_points = np.array(intersection_points)
#ax.scatter(intersection_points[:, 0], intersection_points[:, 1], intersection_points[:, 2], color='g', marker='o')

# Set plot limits
ax.set_xlim(min(line_start[0], line_end[0]) - 1, max(line_start[0], line_end[0]) + 1)
ax.set_ylim(min(line_start[1], line_end[1]) - 1, max(line_start[1], line_end[1]) + 1)
ax.set_zlim(min(line_start[2], line_end[2]) - 1, max(line_start[2], line_end[2]) + 1)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
