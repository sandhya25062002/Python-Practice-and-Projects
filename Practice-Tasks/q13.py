"""
Write a function that accepts a number and prints its multiplication table from 1 to 10.

"""

def print_table(number):

    for i in range (1 , 11):
        print(f"{number} X {i} = {number * i}")



num = int(input("Enter number : "))
print_table(num)