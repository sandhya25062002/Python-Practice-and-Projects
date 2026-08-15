"""
Write a function that accepts a list of strings and returns the longest string in the list.
"""

def longest_string(string_list):
    longest = string_list[0]

    for word in string_list:
        if len(word) > len(longest):
            longest = word

    return longest


words = (input("Enter string seprated by space : ").split())

print(longest_string(words))
