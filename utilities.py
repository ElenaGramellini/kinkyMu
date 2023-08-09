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
        
        # Define the ranges
        self.xRange = [-0.5*self.width, 0.5*self.width]
        self.yRange = [-0.5*self.depth, 0.5*self.depth]
        self.zRange = [self.height/2., self.height/2.]
        self.thetaRange  = [0., 0.25*math.pi]
        self.phiRange    = [0., 2*math.pi]
        self.energyRange = [1., 20.]

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
        self.energy =  random.uniform(self.energyRange[0], self.energyRange[1])  
        #print (self.energy,  self.theta)

    def metadata(self):
        #data = [CR distribution x, y, z, theta, Energy,
        #        Detector w, l, h, pos x, pos y, pos z]        
        line = "## The CR distribution is: \n"
        line += "## " + "uniform"  + " in x      between "+ str(self.xRange) + "\n"   
        line += "## " + "uniform"  + " in y      between "+ str(self.yRange) + "\n"   
        line += "## " + "uniform"  + " in z      between "+ str(self.zRange) + "\n"   
        line += "## " + "uniform"  + " in phi    between "+ str(self.phiRange)    + "\n"   
        line += "## " + "gaussian" + " in theta  between "+ str(self.thetaRange)  + "\n"   
        line += "## " + "uniform"  + " in energy between "+ str(self.energyRange) + "\n"  
        return line

            
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

    def calculateLenght(self):
        length = 0.
        return length

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
