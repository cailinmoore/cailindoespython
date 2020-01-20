#!/usr/bin/env python

from math import pi 

def cylinder_volume(radius, height):
    """
    Function to calculate the volume of a cylinder for given radius and height

    Inputs
    radius: radius of cylinder
    height: height of cylinder

    Returns
    vol: volume
    """
    if radius < 0 or height < 0:
        raise ValueError
    else:
        vol = height*pi*radius**2
        return vol
        
        

def torus_volume(r1, r2):
    """
    Function to calculate the volume of a torus for given radius and height

    Inputs
    r1,r2: input radii

    Returns
    vol: volume
    """
    if r1 < 0 or r2 < 0:
        raise ValueError
    else:
        if r1>r2:
            outerR = r1
            innerR = r2
        else:
            innerR = r1
            outerR = r2
        r = (outerR - innerR)/2 #minor radius
        R = innerR + r #major radius

        vol = (pi*r**2)*(2*pi*R)

        return vol
        


if __name__ == "__main__":
    cy = cylinder_volume(10,2)
    print('Cylinder volume:')
    print(cy)

    tor = torus_volume(20,5)
    print('Torus Volume:')
    print(tor)
