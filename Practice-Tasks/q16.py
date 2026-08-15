"""
Write a function that accepts a number and returns the sum of its digits.
"""

def sum_of_digit(number):
    num_str = str(number)
    total = 0

    for num in num_str:
        total += int(num)

    return total


nums = int(input("Enter a number : "))

print(sum_of_digit(nums))