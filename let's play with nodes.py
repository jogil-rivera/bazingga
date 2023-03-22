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


