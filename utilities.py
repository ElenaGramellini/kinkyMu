import math
import random
import numpy as np
import csv


class DetectorBox:
    def __init__(self, center_x, center_y, center_z, width, depth, height):
        self.center_x = center_x
        self.center_y = center_y
        self.center_z = center_z
        self.width = width
        self.depth = depth
        self.height = height
        
    def get_corner_points(self):
        half_width = self.width / 2
        half_height = self.height / 2
        half_depth = self.depth / 2

        x = [
            self.center_x - half_width, self.center_x - half_width,
            self.center_x + half_width, self.center_x + half_width,
            self.center_x - half_width, self.center_x - half_width,
            self.center_x + half_width, self.center_x + half_width
        ]
        y = [
            self.center_y - half_depth, self.center_y + half_depth,
            self.center_y + half_depth, self.center_y - half_depth,
            self.center_y - half_depth, self.center_y + half_depth,
            self.center_y + half_depth, self.center_y - half_depth
        ]
        z = [
            self.center_z - half_height, self.center_z - half_height,
            self.center_z - half_height, self.center_z - half_height,
            self.center_z + half_height, self.center_z + half_height,
            self.center_z + half_height, self.center_z + half_height
        ]

        return x, y, z

    def get_dimensions(self):
        return  np.array([self.width, self.depth, self.height])

    def get_center(self):
        return np.array([self.center_x, self.center_y, self.center_z])
        
    def describe(self):
        print("The detector location is: ")
        print("(",self.center_x, self.center_y, self.center_z,")")
        print("The detector dimensions are:")
        print("W (x):",self.width,"; D (y):",self.depth,"; H (z):",self.height)
    


class CosmicRay(DetectorBox):
    def __init__(self, center_x, center_y, center_z, width, depth, height, momentum, x, y, z, theta, phi):
        super().__init__(center_x, center_y, center_z, width, depth, height)
        self.momentum = momentum
        self.x = x
        self.y = y
        self.z = z
        self.theta = theta # in rad
        self.phi   = phi   # in rad

        
    def __init__(self, box):
        super().__init__(box.center_x, box.center_y, box.center_z, box.width, box.depth, box.height)
        #self.x = random.uniform(-5*self.width, 5*self.width)
        #self.y = random.uniform(-5*self.depth, 5*self.depth)
        
        # Define the ranges
        self.xRange = [-0.5*self.width, 0.5*self.width]
        self.yRange = [-0.5*self.depth, 0.5*self.depth]
        self.zRange = [self.height/2., self.height/2.]
        self.thetaRange  = [0., 0.25*math.pi]
        self.phiRange    = [0., 2*math.pi]
        self.momentumRange = [1., 20.]

        # Define the throwing functions 
        self.x   = random.uniform(self.xRange[0], self.xRange[1])
        self.y   = random.uniform(self.yRange[0], self.yRange[1])
        self.z   = self.zRange[0]
        self.phi = random.uniform(self.phiRange[0], self.phiRange[1])
        ###
        # Mean and covariance matrix of the Gaussian distribution
        #mean = [0., 10 ]
        #cov = [[0.25*math.pi, 0.25*math.pi], [0.25*math.pi, 0.25*math.pi]]
        # Generate two random numbers from the 2D Gaussian distribution
        #r = np.random.multivariate_normal(mean, cov, 1).T
        
        self.theta  =  np.random.normal(self.thetaRange[0], self.thetaRange[1],1)[0]  
        self.momentum =  random.uniform(self.momentumRange[0], self.momentumRange[1])

        #print (self.momentum,  self.theta)

    def metadata(self):
        #data = [CR distribution x, y, z, theta, Momentum,
        #        Detector w, l, h, pos x, pos y, pos z]        
        line = "## The CR distribution is: \n"
        line += "## " + "uniform"  + " in x      between "+ str(self.xRange) + "\n"   
        line += "## " + "uniform"  + " in y      between "+ str(self.yRange) + "\n"   
        line += "## " + "uniform"  + " in z      between "+ str(self.zRange) + "\n"   
        line += "## " + "uniform"  + " in phi    between "+ str(self.phiRange)    + "\n"   
        line += "## " + "gaussian" + " in theta  between "+ str(self.thetaRange)  + "\n"   
        line += "## " + "uniform"  + " in momentum between "+ str(self.momentumRange) + "\n"  
        return line


    def display_info(self):
        print("Cosmic Ray Information:")
        print("Momentum:", self.momentum)
        print("Position (x, y, z):", self.x, self.y, self.z)
        print("Angles (theta, phi):", self.theta, self.phi)

    def line_equation(self):
        # Compute direction cosines
        cos_theta = math.cos(self.theta)
        sin_theta = math.sin(self.theta)
        cos_phi = math.cos(self.phi)
        sin_phi = math.sin(self.phi)
        
        # Compute direction vector
        dx = sin_theta * cos_phi 
        dy = sin_theta * sin_phi
        dz = cos_theta
        
        # Define the parametric equations
        x1 = f"x1 = {self.x} + t * {dx}"
        y1 = f"y1 = {self.y} + t * {dy}"
        z1 = f"z1 = {self.z} + t * {dz}"

        return x1, y1, z1


    def line_parameters(self):
        # Compute direction cosines
        cos_theta = math.cos(self.theta)
        sin_theta = math.sin(self.theta)
        cos_phi = math.cos(self.phi)
        sin_phi = math.sin(self.phi)
        
        # Compute direction vector
        dx = sin_theta * cos_phi 
        dy = sin_theta * sin_phi
        dz = cos_theta

        return self.x, self.y, self.z1, dx, dy, dz

    # compute line CR line beginning and end for visualization purpose
    def ends(self):
        # Compute direction cosines
        cos_theta = math.cos(self.theta)
        sin_theta = math.sin(self.theta)
        cos_phi = math.cos(self.phi)
        sin_phi = math.sin(self.phi)
        
        # Compute direction vector
        dx = sin_theta * cos_phi 
        dy = sin_theta * sin_phi
        dz = cos_theta
        
        # Define the parametric equations
        z1 = -0.75*self.height # we want the CR to end just under the detector
        t  = (z1 - self.z)/dz    
        x1 = self.x + t * dx
        y1 = self.y + t * dy
        begin = [self.x, self.y, self.z]
        end   = [x1, y1, z1]  
        return (begin , end)

    def plane_normal_from_points(self, point1, point2, point3):
        vector1 = np.array(point2) - np.array(point1)
        vector2 = np.array(point3) - np.array(point1)
        normal_vector = np.cross(vector1, vector2)
        #print(len(normal_vector))
        return normal_vector

    def line_direction_from_points(self, point1, point2):
        return np.array(point2) - np.array(point1)

    def line_plane_intersection(self, line_point, line_direction, plane_normal, plane_point):
        # Calculate the parameter t
        t = -np.dot(plane_normal, line_point - plane_point) / np.dot(plane_normal, line_direction)
        # Calculate the intersection point
        intersection_point = line_point + t * line_direction
        return intersection_point


    def plane_CR_intersection(self, p1, p2, p3, pl1, pl2):
        plane_normal       = self.plane_normal_from_points(p1, p2, p3)
        line_direction     = self.line_direction_from_points(pl1, pl2)
        intersection_point = self.line_plane_intersection(pl1,line_direction, plane_normal, p1 )
        # Check if plane and line intersect
        has_nan = np.any(np.isnan(intersection_point))
        has_inf = np.any(np.isinf(intersection_point))
        # if they do, return the intersection point
        # if they don't return False
        #print("in plane_CR_intersection --> nan", has_nan, "inf", has_inf)
        if has_nan or has_inf:
            return np.array([False])
        return intersection_point

    def boundaryChecker(self, p):
        tolerance = 0.0000000000001
        width  = (self.width )/2. + tolerance
        depth  = (self.depth )/2. + tolerance
        height = (self.height)/2. + tolerance
        #print("In boundary checking ----->", p, width, depth, height)
        if p[0] > width :
            #print("failed ", p[0], " > ", width)
            return False
        if p[0] < (-1.*width):
            #print("failed ", p[0], " < ", -1.*width)
            return False
        if p[1] > depth :
            #print("failed ", p[1], " > ", depth)
            return False
        if p[1] < (-1.*depth) :
            #print("failed ", p[1], " < ", -1.*depth)
            return False
        if p[2] > height :
            #print("failed ", p[2], " > ", height)
            return False
        if p[2] < (-1*height) :
            #print("failed ", p[2], " < ", -1*height)
            return False
        return True
    
    def calculateMaxLenght(self):
        length = self.momentum
        return length

    def calculateLenght(self):
        width  = self.width
        depth  = self.depth
        height = self.height
        ends   = self.ends()
        pl1    = np.array(ends[0])
        pl2    = np.array(ends[1])
        #print("calculate lenght")
        crossing_point_list = []
        p1 = [ 1, 0, height/2.]
        p2 = [-1, 0, height/2.]
        p3 = [ 0, 1, height/2.]
        z_top = self.plane_CR_intersection(p1, p2, p3, pl1, pl2)
        if np.any(z_top) and self.boundaryChecker(z_top):
            crossing_point_list.append(z_top)
        p1 = [ 1, 0, height/(-2.)]
        p2 = [-1, 0, height/(-2.)]
        p3 = [ 0, 1, height/(-2.)]
        z_bottom = self.plane_CR_intersection(p1, p2, p3, pl1, pl2)
        if np.any(z_bottom) and self.boundaryChecker(z_bottom):
            crossing_point_list.append(z_bottom)
        p1 = [ 1, depth/2., 0]
        p2 = [-1, depth/2., 0]
        p3 = [ 0, depth/2., 1]
        y_top = self.plane_CR_intersection(p1, p2, p3, pl1, pl2)
        if np.any(y_top) and self.boundaryChecker(y_top):
            crossing_point_list.append(y_top)
        p1 = [ 1, depth/(-2.), 0]
        p2 = [-1, depth/(-2.), 0]
        p3 = [ 0, depth/(-2.), 1]
        y_bottom = self.plane_CR_intersection(p1, p2, p3, pl1, pl2)
        if np.any(y_bottom) and self.boundaryChecker(y_bottom):
            crossing_point_list.append(y_bottom)
        p1 = [width/2.   , 0, 1 ]
        p2 = [width/2.   , 0,-1 ]
        p3 = [width/2.   , 1, 0 ]
        x_top = self.plane_CR_intersection(p1, p2, p3, pl1, pl2)
        if np.any(x_top) and self.boundaryChecker(x_top):
            crossing_point_list.append(x_top)
        p1 = [width/(-2.), 0, 1 ]
        p2 = [width/(-2.), 0,-1 ]
        p3 = [width/(-2.), 1, 0 ]
        x_bottom = self.plane_CR_intersection(p1, p2, p3, pl1, pl2)
        if np.any(x_bottom) and self.boundaryChecker(x_bottom):
            crossing_point_list.append(x_bottom)
        if len(crossing_point_list) == 0:
            #print("Not crossing")
            return -99999. 
        if len(crossing_point_list) != 2:
            print("Debug")
            print(crossing_point_list, len(crossing_point_list))
            print("Impossible result, GO FIND THIS BUG.... ")
            print("x_top    ",x_top, self.boundaryChecker(x_top))
            print("x_bottom ",x_bottom, self.boundaryChecker(x_bottom))
            print("y_top    ",y_top, self.boundaryChecker(y_top))
            print("y_bottom ",y_bottom, self.boundaryChecker(y_bottom))
            print("z_top    ",z_top, self.boundaryChecker(z_top))
            print("z_bottom ",z_bottom, self.boundaryChecker(z_bottom))
            print()
            print(self.x , self.y ,  self.z , np.degrees(self.theta) , np.degrees(self.phi))
            print()
            return -99999.
        calculated_length =  np.linalg.norm(crossing_point_list[0] - crossing_point_list[1])
        maxLength = self.calculateMaxLenght()
        if calculated_length < maxLength:
            return maxLength
        #print("Lenght ------------->", calculated_length)
        return calculated_length



class EventWriter:
    def __init__(self, filename):
        self.filename = filename

    def metadataWriter(self, data):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            file.write( "##\n" )
            file.write( "## Metadata\n" )
            file.write( "##\n" )
            file.write( data[0] )
            file.write( "##\n" )
            file.write("## The detector dimensions W x D x H are: "+ str(data[1])+ "\n" )
            file.write("## The detector center is at "+ str(data[2])+"\n" )
            file.write( "##\n" )
            file.write( "##\n\n\n\n" )
            
    def headerWriter(self, headers):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

    def writeEvent(self, event_data):
        with open(self.filename, mode='a', newline='') as file:            
            expected_length = 4
            # Check the length of the list
            if len(event_data) != expected_length:
                raise ValueError(f"List length should be {expected_length}, but it is {len(event_data)}.")

            # Check for NaN values in the list
            has_nan = any(math.isnan(x) for x in event_data)
            if has_nan:
                raise ValueError("List contains NaN values.")
            
            # if all good, write event
            writer = csv.writer(file)
            writer.writerow(event_data)
