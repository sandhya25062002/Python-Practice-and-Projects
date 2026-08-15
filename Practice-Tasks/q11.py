"""
 Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.
"""

def squares_number(numbers):
    new_list = []

    for num in numbers:
      new_list.append(num * num)
    return new_list


nums = list(map(int,input("Enter numbers seprated by space : ").split()))

print(squares_number(nums))