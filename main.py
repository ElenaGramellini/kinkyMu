import matplotlib.pyplot as plt
from utilities import DetectorBox
from utilities import CosmicRay

## Let's define the position and dimensions of the detector box
## cause we need to calculate the cosmics in the box

#pDUNE = DetectorBox(0, 0, 0, 7.2, 7.1, 6)
pDUNE = DetectorBox(0, 0, 0, 2, 10, 30)
pDUNE.describe()

x      = []
y      = []
z      = []
energy = []
theta  = []
phi    = []

for i in range(100000):
    cr = CosmicRay(pDUNE)
    x      .append(cr.x      )
    y      .append(cr.y      )
    z      .append(cr.z      )
    energy .append(cr.energy )
    theta  .append(cr.theta  )
    phi    .append(cr.phi    )

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
axs[1, 1].set_title('Theta [deg]')

# Plot in the sixth subplot (bottom-right)
axs[1, 2].hist(phi)
axs[1, 2].set_title('Phi [deg]')

# Adjust spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
