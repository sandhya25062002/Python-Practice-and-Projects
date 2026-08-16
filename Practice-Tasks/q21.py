"""
Write a function that accepts a string and returns the first non-repeating character in the string.
"""

def non_repeating_char(string):

    for ch in string:
        if string.count(ch)== 1:
            return ch

    return None



text = input("Enter string : ")

print(non_repeating_char(text))


