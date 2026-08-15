"""
Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase
 using a function.
"""

def convert_case(s):
    if len(s) > 5 :
        return s.upper()

    else:
        return s.lower()


text = input("Enter text : ")   

print(convert_case(text))


