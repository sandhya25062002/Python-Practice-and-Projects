"""
 Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.

"""

def divisible_by_3(numbers):

    new_list = []

    for num in numbers:
        if num % 3 == 0:
            new_list.append(num)

    return new_list


nums = list(map(int,input("Enter a number seprated by space : ").split()))

print(divisible_by_3(nums))

