import matplotlib.pyplot as plt
from utilities import DetectorBox
from utilities import CosmicRay
from utilities import EventWriter
from vis import Display
import time


#Let's start with initializing things

# Do I want a small display of the cosmic rays?
DISPLAY = False
# Number of events to be generated
Nevt = 10000 
start_time = time.time()

# Let's instatiate the visualization tool
if DISPLAY:
    display = Display()

## Let's define the position and dimensions of the detector box
## cause we need to calculate the cosmics in the box
pDUNE = DetectorBox(0, 0, 0, 7.2, 7.1, 6)
#pDUNE = DetectorBox(0, 0, 0, 2, 10, 30)
pDUNE.describe()

# let's define a cosmic ray
cr = CosmicRay(pDUNE)

x      = []
y      = []
z      = []
energy = []
theta  = []
phi    = []



# Open and write output file
# Create an instance of the EventWriter class and specify the filename
event_writer = EventWriter('CR_Energy_L_events.csv')
# Define the metadata for the CSV file
metadata = [cr.metadata(), pDUNE.get_dimensions(), pDUNE.get_center()]
event_writer.metadataWriter(metadata)
# Define the header for the CSV file
header = ['Event_ID', 'Energy', 'Lenght', 'Theta']
# Write the header to the CSV file
event_writer.headerWriter(header)

# Let's generate Nevt events
for i in range(Nevt):
    cr = CosmicRay(pDUNE) # I need to re-call to regenerate the random number
    this_x      = cr.x      
    this_y      = cr.y      
    this_z      = cr.z      
    this_energy = cr.energy 
    this_theta  = cr.theta  
    this_phi    = cr.phi    
    length      = cr.calculateLenght()

    # Write important bits to file
    event_writer.writeEvent([i, this_energy, length, this_theta])

    # The following array are for plotting purposes only
    x      .append(this_x      )
    y      .append(this_y      )
    z      .append(this_z      )
    energy .append(this_energy )
    theta  .append(this_theta  )
    phi    .append(this_phi    )
    
    # Let's add a little display tool
    if i < 10 and DISPLAY:
        display.plot_line(cr.ends()) # beginning and end of line

end_time = time.time()
# Calculate the execution time
execution_time = (end_time - start_time)/60.
# Print the execution time
print("Generating ", Nevt, "events in ")
print(f"{execution_time:.3f} minutes")
        
# Create the figure and subplots
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
# Plot in the first subplot (top-left)
axs[0, 0].hist(x)
axs[0, 0].set_title('x [m]')

# Plot in the second subplot (top-center)
axs[0, 1].hist(y)
axs[0, 1].set_title('y [m]')

# Plot in the third subplot (top-right)
axs[0, 2].hist(z)
axs[0, 2].set_title('z [m]')

# Plot in the fourth subplot (bottom-left)
axs[1, 0].hist(energy)
axs[1, 0].set_title('Energy [GeV]')

# Plot in the fifth subplot (bottom-center)
axs[1, 1].hist(theta)
axs[1, 1].set_title('Theta [rad]')

# Plot in the sixth subplot (bottom-right)
axs[1, 2].hist(phi)
axs[1, 2].set_title('Phi [rad]')

# Adjust spacing between subplots
plt.tight_layout()

# Show the figure
if DISPLAY:
    display.plot_box(pDUNE.get_center(), pDUNE.get_dimensions() )  # center box and dimensions
    display.set_limits(-1.*pDUNE.get_dimensions(), pDUNE.get_dimensions()) 
    display.set_labels('X', 'Y', 'Z')
    display.set_title('Cosmic And Detector Visualization')

plt.show()
