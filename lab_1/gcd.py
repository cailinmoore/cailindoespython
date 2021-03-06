#!/usr/bin/env python

from math import gcd as gcdNative
import random

def gcd(x,y):
    ''' This function computes the greatest common denominator of two input values without using 
    math package gcd 

    parameters: x and y are numbers you are looking for a greatest common denominator for 
    returns: x is the greatest common denominator of inputs x and y 
    '''
    
    #code taken from https://www.geeksforgeeks.org/gcd-in-python/
    while y:
        x, y = y, x % y

    return x 

if __name__ == "__main__":
    a = random.randint(1,100)
    b = random.randint(1,100)
    answer = gcdNative(a,b)
    check = gcd(a,b)

    if answer == check:
        print("Nice they are the same!")
    else:
        print("Looks like your code doesn't work!")
        
    print('With a of', a, 'and b of', b, 'gcdNative returns', answer, 'and my function returns', check)