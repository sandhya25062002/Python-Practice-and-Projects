"""
Write a function that accepts a string and returns True if the string is a palindrome, and False otherwise.

"""

def palindrom(s):
   result = ""  # empty string

   for ch in s:
      result = ch + result   # string reverse

   if result == s:
      return True
   else:
      return False


string = input("Enter string : ")

if palindrom(string):
   print("string is palindrom")

else:
   print("string is not palindrom")
   
