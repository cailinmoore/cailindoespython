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
        
        

def torus_volume(innerR, outerR):
    """
    Function to calculate the volume of a torus for given radius and height

    Inputs
    innerR, outerR: input radii

    Returns
    vol: volume
    """
    if innerR < 0 or outerR < 0:
        raise ValueError
    elif innerR > outerR:
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

    tor = torus_volume(20,5)
    print('Torus Volume:')
    print(tor)
