#!/usr/bin/env python

def letter_count(string, letter):
    """
        Function to count instances of letters in words case insensitive. 
        Inputs-
        string: string to search
        letter: character to search for in string

        Returns 
        num: number of instances  
    """
    
    num = string.lower().count(letter)
    if num == 0:
        print("Oops! Looks like that letter isn't in that word.")
    else:
        return num

if __name__ == "__main__":
    test = letter_count("heLlo", 'l')
    print(test)

