#!/usr/bin/env python

from math import pi 

def cylinder_volume(radius, height):
    #calculate the volume of a cylinder for given radius and height
    if radius < 0 or height < 0:
        raise ValueError
    else:
        vol = height*pi*radius**2
        return vol
        
        

def torus_volume(outerR, innerR):
    #Return the volume of a torus for given radii 
    if outerR < 0 or innerR < 0:
        raise ValueError
    else:
        r = (outerR - innerR)/2 #minor radius
        R = innerR + r #major radius

        vol = (pi*r**2)*(2*pi*R)

        return vol
        


if __name__ == "__main__":
    cy = cylinder_volume(10,2)
    print('Cylinder volume:')
    print(cy)

    tor = torus_volume(2,5)
    print('Torus Volume:')
    print(tor)
