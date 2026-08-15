"""
Write a function that accepts a number and checks if it is an Armstrong number.
"""

def is_armstrong(num):
    num_str = str(num)

    num_digits = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits

    return total == num


num = int(input("Enter a number : "))

if is_armstrong(num):
    print(f"{num} is an armstrong number")

else:
    print(f"{num} is not an armstrong number")

