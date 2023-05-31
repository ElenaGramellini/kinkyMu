import math
import random
import numpy as np

class DetectorBox:
    def __init__(self, center_x, center_y, center_z, width, height, depth):
        self.center_x = center_x
        self.center_y = center_y
        self.center_z = center_z
        self.width = width
        self.height = height
        self.depth = depth

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
            self.center_y - half_height, self.center_y + half_height,
            self.center_y + half_height, self.center_y - half_height,
            self.center_y - half_height, self.center_y + half_height,
            self.center_y + half_height, self.center_y - half_height
        ]
        z = [
            self.center_z - half_depth, self.center_z - half_depth,
            self.center_z - half_depth, self.center_z - half_depth,
            self.center_z + half_depth, self.center_z + half_depth,
            self.center_z + half_depth, self.center_z + half_depth
        ]

        return x, y, z

    def describe(self):
        print("The detector location is: ")
        print("(",self.center_x, self.center_y, self.center_z,")")
        print("The detector dimensions are:")
        print("W (x):",self.width,"; D (y):",self.depth,"; H (z):",self.height)
    


class CosmicRay(DetectorBox):
    def __init__(self, center_x, center_y, center_z, width, height, depth, energy, x, y, z, theta, phi):
        super().__init__(center_x, center_y, center_z, width, height, depth)
        self.energy = energy
        self.x = x
        self.y = y
        self.z = z
        self.theta = theta # in rad
        self.phi   = phi   # in rad

    def __init__(self, box):
        super().__init__(box.center_x, box.center_y, box.center_z, box.width, box.height, box.depth)
        self.x = random.uniform(-5*self.width, 5*self.width)
        self.y = random.uniform(-5*self.depth, 5*self.depth)
        self.z = self.height/2.
        self.phi   = random.uniform(0, 2*math.pi)
        ###
        # Mean and covariance matrix of the Gaussian distribution
        mean = [2, 0]
        cov = [[1, 0.5], [0.5, 1]]
        # Generate two random numbers from the 2D Gaussian distribution
        r = np.random.multivariate_normal(mean, cov, 1).T
        #print(r.shape)
        self.theta  = (r[0])[0]
        self.energy = (r[1])[0]
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
        dx = cos_theta * sin_phi
        dy = sin_theta * sin_phi
        dz = cos_phi
        
        # Define the parametric equations
        x1 = f"x1 = {self.x} + t * {dx}"
        y1 = f"y1 = {self.y} + t * {dy}"
        z1 = f"z1 = {self.z} + t * {dz}"

        return x1, y1, z1

