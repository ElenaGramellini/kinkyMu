import math
import random
import numpy as np

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
    def __init__(self, center_x, center_y, center_z, width, depth, height, energy, x, y, z, theta, phi):
        super().__init__(center_x, center_y, center_z, width, depth, height)
        self.energy = energy
        self.x = x
        self.y = y
        self.z = z
        self.theta = theta # in rad
        self.phi   = phi   # in rad

    def __init__(self, box):
        super().__init__(box.center_x, box.center_y, box.center_z, box.width, box.depth, box.height)
        #self.x = random.uniform(-5*self.width, 5*self.width)
        #self.y = random.uniform(-5*self.depth, 5*self.depth)
        self.x   = random.uniform(-0.5*self.width, 0.5*self.width)
        self.y   = random.uniform(-0.5*self.depth, 0.5*self.depth)
        self.z   = self.height/2.
        self.phi = random.uniform(0, 2*math.pi)
        ###
        # Mean and covariance matrix of the Gaussian distribution
        #mean = [0., 10 ]
        #cov = [[0.25*math.pi, 0.25*math.pi], [0.25*math.pi, 0.25*math.pi]]
        # Generate two random numbers from the 2D Gaussian distribution
        #r = np.random.multivariate_normal(mean, cov, 1).T
        
        self.theta  =  np.random.normal(0., 0.25*math.pi,1)[0]  
        self.energy =  random.uniform(1, 20)  
        #print (self.energy,  self.theta)
        
    def display_info(self):
        print("Cosmic Ray Information:")
        print("Energy:", self.Energy)
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

