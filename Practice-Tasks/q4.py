"""
Write a function that accepts a list of numbers and returns the maximum value in the list.

"""

def max_value(numbers):
    largest_value = numbers[0]

    for num in numbers:
        if num > largest_value:
            largest_value = num

    return largest_value


nums = list(map(int,input("Enter number sperated by space : ").split()))

print(f"maximum value : {max_value(nums)}")