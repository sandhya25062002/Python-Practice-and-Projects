"""
Write a function that accepts a list of numbers and returns the average of the numbers.
"""

def average(numbers):
    total = 0

    for num in numbers:
        total += num

    avg = total / len(numbers)
    return avg



nums = list(map(int,input("Enter number seprated by space : ").split()))

print(average(nums))