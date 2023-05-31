# kinkyMu
Draft of work and code organization.
Let's start from the end: I want to provide a 2D pdf in (Energy, Length) for muons in a mock detector geometry.
What we need:
[  ] a realistic muon flux
     [ X ] Find the paper for the flux: it's a function of (Energy, Polar Angle).
           The assumption is that the flux doesn't change in the azimuthal angle, and in height.  
     [ X ] Code the Phi (Energy, Polar Angle)
     [   ] Check it's correct against data reported in the paper
          [   ] Find the data
	  [   ] Solve normalization issue
[  ] the correct implementation of said muon flux
     [ X ] Write a simple (En, x,y,z,theta,phi) 6D flat distribution
     [ X ] Write a unit code that checks that flat distribution
     [ X ] Implement z = fixed, (x,y,phi) = flat,  (En, theta) = Phi(En,theta) generator
     [   ] Implement (En, theta) = 2D gaussian
     [   ] Implement (En, theta) = Phi(En,theta) generator	
     [   ] Check I get what I want with the unit code
     [   ] Check I get what I want with the unit code
[  ] to calculate the lenght inside mock detector
[  ] to check the calculation is correct
     [   ] Check I get what I want with the unit code
