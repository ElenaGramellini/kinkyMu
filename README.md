# kinkyMu
Just run
> python main.py
for main simulation of cosmic rays


Output:
File with a header and event list.
The header listis the simulation conditions:
 - x,y,z, phi, theta energy distributions
 - detector size and location

Event list has 4 columns:
- Event ID, Energy, Lenght, theta


Draft of work and code organization.
Let's start from the end: I want to provide a 2D pdf in (Energy, Length) for muons in a mock detector geometry.
What we need:
[  ] a realistic muon flux
     [ X ] Find the paper for the flux: it's a function of (Energy, Polar Angle).
           The assumption is that the flux doesn't change in the azimuthal angle, and in height.  
     [ X ] Code the Phi (Energy, Polar Angle)
     [   ] Check it's correct against data reported in the paper
          [ X ] Find the data
	  [ X ] Solve normalization issue --> we don't care about the normalization, cause we need a PDF
[  ] the correct implementation of said muon flux
     [ X ] Write a simple (En, x,y,z,theta,phi) 6D flat distribution
     [ X ] Write a unit code that checks that flat distribution
     [ X ] Implement z = fixed, (x,y,phi) = flat,  (En, theta) = Phi(En,theta) generator
     [   ] Write a random Generator of the flux (En, theta) = Phi(En,theta) generator	

[ X ] to calculate the lenght inside mock detector
[ X ] to check the calculation is correct
     [   ] Check I get what I want with the unit code

[ X ] write output file