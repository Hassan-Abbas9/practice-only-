# Q1) check balanced paranthesis. The paranthesis can be only ( or )
# Ex: INPUT ---> " (( ))"
# Output --> True
# Input ---> ")()()("
# Output ---> False


def check_if_balanced_paranthesis(list):
    stack = []

    for str in list:  # for each character inside the list, if the character is ( we add it to stack and we add it to stack
        if str == '(':
            stack.append(str)
        elif str == ')':  # for each character inside the list, if length is 0 we return false
            if len(stack) == 0:
                return False
            else:  # if length not 0 means ')' is still inside the list, so we pop it out.
                stack.pop()
    return len(stack) == 0


str= "(())"
print(check_if_balanced_paranthesis(str))
str = "(3+5*(2-5)"
print(check_if_balanced_paranthesis(str))
