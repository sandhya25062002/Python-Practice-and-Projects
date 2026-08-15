"""
Write a function that accepts a string and a character, and returns the number of times the character appears in the string.

"""

def count_char(s , char):
    count = 0

    for ch in s:
        if ch == char:
            count += 1

    return count


string = input("Enter string : ")
character = input("Enter one character : ")

print(f"{character} appears {count_char(string,character)} times")