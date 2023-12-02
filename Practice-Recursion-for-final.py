# Problem 1: Factorial
#
# Write a recursive function to calculate the factorial of a given positive integer n.
# The factorial of n is the product of all positive integers up to n.
# n!=n×(n−1)×(n−2)×…×2×1

def factorial(num):
    if num ==0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))
