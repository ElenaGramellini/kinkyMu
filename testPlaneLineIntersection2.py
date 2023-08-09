import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plane_normal_from_points(point1, point2, point3):
    vector1 = np.array(point2) - np.array(point1)
    vector2 = np.array(point3) - np.array(point1)
    normal_vector = np.cross(vector1, vector2)
    print(len(normal_vector))
    return normal_vector

def plane_equation_from_points(point1, point2, point3):
    vector1 = np.array(point2) - np.array(point1)
    vector2 = np.array(point3) - np.array(point1)
    normal_vector = np.cross(vector1, vector2)
    A, B, C = normal_vector
    D = -np.dot(normal_vector, np.array(point1))
    return A, B, C, D

def line_direction_from_points(point1, point2):
    return np.array(point2) - np.array(point1)

def line_plane_intersection(line_point, line_direction, plane_normal, plane_point):
    # Calculate the parameter t
    t = -np.dot(plane_normal, line_point - plane_point) / np.dot(plane_normal, line_direction)
    # Calculate the intersection point
    intersection_point = line_point + t * line_direction
    return intersection_point


def plane_CR_intersection(p1, p2, p3, pl1, pl2):
    plane_normal = plane_normal_from_points(p1, p2, p3)
    line_direction = line_direction_from_points(pl1, pl2)
    intersection_point = line_plane_intersection(pl1,line_direction, plane_normal, p1 )
    # Check if plane and line intersect
    has_nan = np.any(np.isnan(intersection_point))
    has_inf = np.any(np.isinf(intersection_point))
    #print("--------->", intersection_point, has_nan*has_inf)
    # if they do, return the intersection point
    # if they don't return False
    if has_nan and has_inf:
        return intersection_point
    return (has_nan and has_inf)
    

def calculateLenght(width, depth, height, pl1, pl2):
    print("calculate lenght")
    p1 = [ 1, 0, height/2.]
    p2 = [-1, 0, height/2.]
    p3 = [ 0, 1, height/2.]
    z_top = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    p1 = [ 1, 0, height/(-2.)]
    p2 = [-1, 0, height/(-2.)]
    p3 = [ 0, 1, height/(-2.)]
    z_bottom = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    p1 = [ 1, depth/2., 0]
    p2 = [-1, depth/2., 0]
    p3 = [ 0, depth/2., 1]
    y_top = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    p1 = [ 1, depth/(-2.), 0]
    p2 = [-1, depth/(-2.), 0]
    p3 = [ 0, depth/(-2.), 1]
    y_bottom = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    p1 = [width/2.   , 0, 1 ]
    p2 = [width/2.   , 0,-1 ]
    p3 = [width/2.   , 1, 0 ]
    x_top = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    p1 = [width/(-2.), 0, 1 ]
    p2 = [width/(-2.), 0,-1 ]
    p3 = [width/(-2.), 1, 0 ]
    x_bottom = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    print(x_top, x_bottom, y_top, y_bottom, z_top, z_bottom)
    
# Define the points that define the plane
point1 = np.array([ 1, 0, 5])
point2 = np.array([-1, 0, 5])
point3 = np.array([0, 1, 5])

# Define the points that define the line
pl1 = np.array([1, 0, 3])
pl2 = np.array([1, 0, 4])

calculateLenght(5, 4, 10, pl1, pl2)

intersectionX = plane_CR_intersection(point1, point2, point3, pl1, pl2)

# Calculate the equation of the plane
A, B, C, D = plane_equation_from_points(point1, point2, point3)
vector = plane_normal_from_points(point1, point2, point3)
print("VECTOR ----------------->", vector)

# Create a meshgrid for plotting
x_range = np.linspace(min(point1[0], point2[0], point3[0]) - 1,
                      max(point1[0], point2[0], point3[0]) + 1, 50)
y_range = np.linspace(min(point1[1], point2[1], point3[1]) - 1,
                      max(point1[1], point2[1], point3[1]) + 1, 50)
X, Y = np.meshgrid(x_range, y_range)

# Calculate the corresponding z values using the plane equation
Z = (-A * X - B * Y - D) / C

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Plot the line
ax.plot([pl1[0], pl2[0]],
        [pl1[1], pl2[1]],
        [pl1[2], pl2[2]], color='blue')

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5)

# Plot the points that define the plane
ax.scatter(*point1, color='red', marker='o')
ax.scatter(*point2, color='green', marker='o')
ax.scatter(*point3, color='blue', marker='o')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Visualization of a Plane defined by 3 Points')

plt.show()
