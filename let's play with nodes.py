# "Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6
# (denoted as 6!) is 1*2*3*4*5*6 = 720" (prz)
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))

# The factorial of 3 is 6
# The recursive call, explained:
factorial(3)          # 1st call with 3
3 * factorial(2)      # 2nd call with 2
3 * 2 * factorial(1)  # 3rd call with 1
3 * 2 * 1             # return from 3rd call as number=1
3 * 2                 # return from 2nd call
6                     # return from 1st call

# step-by-step process of what is going on:

x = factorial(3)
# it proofs itself.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    # 3 * 2 = 6 is returned
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    # 2 * 1 = 2 is returned
def factorial(n):
    if n == 1:
        return 1
    # 1 is returned
    else:
        return n * factorial(n-1)

# "Our recursion ends when the number reduces to 1. This is called the base condition." (prz)

# reference: https://www.programiz.com/python-programming/recursion -> (prz)

# countdown
def countdown(n):
    print(n)
    if n == 0:
        return # Terminate recursion
    else:
        countdown(n - 1) # Recursive call

num = 5
countdown(num)

# if you have print(), in the function. printing a copy of the function will ultimately result in a NoneType.
# the return, under else:, in line 55, is optional, in this case.
# reference: https://realpython.com/python-recursion/ -> (real)

def count(n):
    if n == 0:
        return 0
    else:
        return count(n - 1)

num = 5
print('The result of a countdown from', num, 'is', count(num))

# the return, under else:, in line 68, isn't optional. without it, the print ends in a NoneType.

# a more concise way to express the countdown from 5:
def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)

countdown(num)
# (real)

# a non-recursive implementation for comparison:
def countdown(n):
    while n >= 0:
        print(n)
        n -= 1 # decrementing augmented assignment operator

countdown(num)
# (real)

# Concise Python Factorial Function:
def clean_factorial(n):
    return 1 if n <= 1 else n * clean_factorial(n - 1)

print(clean_factorial(num))
print(1 * 2 * 3 * 4 * 5)
# (real)

# steps of the factorial, explained:
def steps_factorial(n):
    print(f"steps_factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * steps_factorial(n - 1)
    print(f"-> steps_factorial({n}) returns {return_value}")
    return return_value

print(steps_factorial(num))
# (real)

# a factorial(), without the use of recursion.
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value

print('for loop:', factorial(num))

# a factorial, using reduce() lambda.

from functools import reduce
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])

print('reduce:', factorial(num))

# breaking off, into lambda introductions.

# "the lambda keyword is used to define an anonymous function in Python." (geek)
# "You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression." (geek)

str1 = 'GeeksforGeeks'

# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))
# (geek)
# converted str1, 'GeeksforGeeks', to it's upper-case and reversed it.

# we can check conditions, with the lambda function

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))
# (geek)
#

# reference: geeksforgeeks.org -> (geek)
# From https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/