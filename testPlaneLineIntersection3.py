import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plane_normal_from_points(point1, point2, point3):
    vector1 = np.array(point2) - np.array(point1)
    vector2 = np.array(point3) - np.array(point1)
    normal_vector = np.cross(vector1, vector2)
    #print(len(normal_vector))
    return normal_vector

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
    # if they do, return the intersection point
    # if they don't return False
    #print("in plane_CR_intersection --> nan", has_nan, "inf", has_inf)
    if has_nan or has_inf:
        return np.array([False])
    return intersection_point
    
    

def calculateLenght(width, depth, height, pl1, pl2):
    #print("calculate lenght")
    crossing_point_list = []
    p1 = [ 1, 0, height/2.]
    p2 = [-1, 0, height/2.]
    p3 = [ 0, 1, height/2.]
    z_top = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    if np.any(z_top):
        crossing_point_list.append(z_top)
    p1 = [ 1, 0, height/(-2.)]
    p2 = [-1, 0, height/(-2.)]
    p3 = [ 0, 1, height/(-2.)]
    z_bottom = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    if np.any(z_bottom):
        crossing_point_list.append(z_bottom)
    p1 = [ 1, depth/2., 0]
    p2 = [-1, depth/2., 0]
    p3 = [ 0, depth/2., 1]
    y_top = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    if np.any(y_top):
        crossing_point_list.append(y_top)
    p1 = [ 1, depth/(-2.), 0]
    p2 = [-1, depth/(-2.), 0]
    p3 = [ 0, depth/(-2.), 1]
    y_bottom = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    if np.any(y_bottom):
        crossing_point_list.append(y_bottom)
    p1 = [width/2.   , 0, 1 ]
    p2 = [width/2.   , 0,-1 ]
    p3 = [width/2.   , 1, 0 ]
    x_top = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    if np.any(x_top):
        crossing_point_list.append(x_top)
    p1 = [width/(-2.), 0, 1 ]
    p2 = [width/(-2.), 0,-1 ]
    p3 = [width/(-2.), 1, 0 ]
    x_bottom = plane_CR_intersection(p1, p2, p3, pl1, pl2)
    if np.any(x_bottom):
        crossing_point_list.append(x_bottom)
    if len(crossing_point_list) == 0:
        print("Not crossing")
        return 0. 
    if len(crossing_point_list) != 2:
        print("Impossible result, GO FIND THIS BUG.... ")
        return False
    calculated_length =  np.linalg.norm(crossing_point_list[0] - crossing_point_list[1])
    print("Lenght ------------->", calculated_length)
    return calculated_length
    
# Define the points that define the plane
point1 = np.array([ 1, 0, 5])
point2 = np.array([-1, 0, 5])
point3 = np.array([0, 1, 5])

# Define the points that define the line
pl1 = np.array([1, 0, 3])
pl2 = np.array([1, 0, 4])

print(calculateLenght(5, 4, 10, pl1, pl2))

