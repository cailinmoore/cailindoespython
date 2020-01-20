#!/usr/bin/env python

def close(a,b,c):
    """
    Function returns True if the absolute difference between 
    the first two numbers is less than the third number.  
    """

    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return "Hmm make sure you are entering integer values only!"
    elif abs(a-b) > c or abs(a-b) == c:
        return False
    elif abs(a-b) < c:
        return True
        

if __name__ == "__main__":
    check = close(600, 3, 60)

    if check == False:
        print("Absolute difference is not less than the third number.")
    elif check == True:
        print("Absolute difference is less than the third number.")
    else:
        print("Something's wrong...") 

