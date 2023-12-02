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


# Problem 2: Sum of Digits
#
# Write a recursive function to find the
# sum of the digits of a positive integer n.

def sum_of_digits(digits):
        if digits == 0: # when we get digits // 10 = 0 we just return 0
            return digits # the base case here is this
        else:

            return digits % 10 + sum_of_digits(digits // 10)
            # so an example here is digits % 10 means remainder is THE
            # last digit here so it's 3 + (remainder digits // 10 which is
            # 12 then we get 3 + 2 + 1.

print(sum_of_digits(123))

