"""
Write a function that accepts a list of numbers and returns the product of all the numbers in the list.

"""
def product(numbers):
    result = 1

    for num in numbers:
        result *= num


    return result 


nums = list(map(int,input("Enter number seprated by space : ").split()))

print(product(nums))
