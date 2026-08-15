"""
Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.
"""

def alternate_case(string):

    result = ""

    for index , ch  in enumerate(string):
        if index % 2 == 0:
            result += ch.upper()

        else:
            result += ch.lower()    

    return result 


text = input("Enter string : ")

print(alternate_case(text))
