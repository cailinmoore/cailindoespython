#!/usr/bin/env python
from math import pi 

#Return the volume of a torus for given radii 
innerR = 3 #given radius of the hole
outerR = 4 #radius of entire shape

r = (outerR - innerR)/2 #minor radius
R = innerR + r #major radius

vol = (pi*r**2)*(2*pi*R)

print(vol)