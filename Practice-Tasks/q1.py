"""
Accept a number from the user and find the factorial of the number using a function with a parameter and return type.
"""

def factorial (n):
    result = 1

    for i in range(1 , n + 1):
        result *= i
    return result


num = int(input("Enter a number: "))
print(f"factorial : {factorial(num)}")

