"""
Write a function that accepts a list of integers and returns the second largest number in the list.

"""

def second_largest(numbers):

    sec_largest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            sec_largest = largest
            largest = num

        elif num > sec_largest and num != largest:
            sec_largest = num

    return sec_largest


nums = list(map(int,input("Enter number seprated by space : ").split()))

print(second_largest(nums))