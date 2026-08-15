"""
Write a function that accepts a list of strings and returns a new list with each string reversed.
"""

def reverse_string(str_list):
    new_list = []
   

    for word in str_list:
       reverse = ""
       for ch in word:
           reverse = ch + reverse
       new_list.append(reverse)
       
    return new_list  


string = list(input("Enter words separeted by space : ").split())

print(reverse_string(string))



