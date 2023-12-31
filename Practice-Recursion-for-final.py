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

# Problem 3: Fibonacci Sequence
#
# Write a recursive function to generate the nth term of the Fibonacci sequence.
# The Fibonacci sequence is defined as follows:
# F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

def fibonacci_sequence(num):
    if num <= 1:
        return num
    else:
        return fibonacci_sequence(num-1) + fibonacci_sequence(num-2)
        # F(2)=1+0=1
        # F(3)=1+1=2F(3)=1+1=2
        # F(4)=2+1=3F(4)=2+1=3
        # F(5)=3+2=5F(5)=3+2=5


print(fibonacci_sequence(5))


# Problem 4: Power
#
# Write a recursive function to calculate the result of raising a number base to the power of an integer exponent.

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

print(power(5,5))


# Problem 5: Palindrome
#
# Write a recursive function to check if a given string is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
#

def palindrome_check(string):

    if len(string):
        return 0
    else:
        if string [0] == string[-1]:
            return palindrome_check(string[1:-1])
        else:
            return False


result = palindrome_check('Hello')
if result:
    print('string is palindrome')
else:
    print('string is not a palindrome')


# Problem 6: Reverse a String
#
# Write a recursive function to reverse a given string.
# For example, if the input is "hello," the output should be "olleh."

def reverse_string(s):

        if not s:
            return s
        else:
            return s[-1] + reverse_string(s[:-1])


s = input("Enter the string you want to reverse: ")
print(f'the reversed string is {reverse_string(s)}')

