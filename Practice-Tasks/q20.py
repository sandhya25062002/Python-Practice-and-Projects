"""
Write a function that accepts a list of strings and returns a new list with only the strings that have an odd length.

"""

def odd_length_string(str_list):

    new_list = []

    for word in str_list:
        if  len(word) % 2 != 0:
            new_list.append(word)

    return new_list



text =  input("Enter a string seperated by space : ").split()

print(odd_length_string(text))
