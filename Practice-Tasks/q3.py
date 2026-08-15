"""
Write a function that accepts a list of numbers and returns the sum of all even numbers in the list.

"""

def sum_of_evens(numbers):
    total = 0

    for num in numbers:
        if num % 2 == 0:
            total += num
    return total


nums = list(map(int,input("Enter number sperated by space : ").split()))
print(sum_of_evens(nums))
