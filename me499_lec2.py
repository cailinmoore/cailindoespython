#!/usr/bin/env python

"""
Lecture 3 in ME 499
1/15/2020
"""

L = [1,2,3]
c = 0
#for loop to sum list 
for i in L: 
    c = c+i
print(c)

#recursion method 
def sum_r(L):
    return L[0] + sum_r(L[1:]) #first plus rest 


def zero(f,a,b,epsilon = 1e-10):
    """
    recursion used for finding the zeros of a function. Faster than iteratively because you halve 
    the searching distance each time

    INPUTS: 
    f: equation of line
    a, b: bounds 
    error: closeness to exact 0 
    """
    #midpoint
    c = (a+b)/2

    #y of a and b 
    f_a = f(a)
    f_b = f(b)

    #sign change only if product is negative
    if f_a * f_b >= 0:
        return None
    elif abs(a-b) < epsilon:
        return c #zero is the midpoint 
    else:
        #recursion part 
        f_c = f(c)

        if f_a*f_c < 0:
            return zero(f, a, c, epsilon) #zero somewhere between a and c
        else:
            return zero(f, c, b, epsilon) #zero somewhere between c and b


"""
Files: 

with open('outline', 'w') as f:
    for n in numbers: 
        f.write(str(n)+ '\n')
"""

"""
Lists, tuples, strings
"""

a = list(range(10))
a = (1,2,3) #m



