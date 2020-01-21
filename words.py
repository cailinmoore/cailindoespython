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
    if not(isinstance(string, str)) or not(isinstance(letter, str)):
        raise ValueError
    
    lword = string.lower()
    lletter = letter.lower()
    count = 0
    for i in lword:
        if lletter == i:
            count = count+1
    
    return count

if __name__ == "__main__":
    test = letter_count('helLoworLd', 'L')
    print(test)

