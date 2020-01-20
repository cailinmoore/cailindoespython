#!/usr/bin/env python

def letter_count(string, letter):
    num = string.count(letter)
    if num == 0:
        print("Oops! Looks like that letter isn't in that word.")
    else:
        return num

if __name__ == "__main__":
    test = letter_count("heLlo", 'l')
    print(test)

