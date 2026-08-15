"""
Write a function that accepts a string and counts how many vowels are in the string.
"""

def count_vowels(s):
    count = 0
    vowels = 'AEIOUaeiou'

    for ch in s:
        if ch in vowels:
            count += 1

    return count


text = input("Enter a string : ")

print(count_vowels(text))
