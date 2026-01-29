# FUNCTIONS IN PYTHON

# Reusable block of code that performs a specific task

# Why we use functions:
#  - for reuse of code
# - organized logic
# - to make a program easier to read and maintain

# How to declare a function in python:

# we use the def keyword to define a function. An example below:

def greet():
    print('Hello')

# The function above will automatically greet the user when called.

def showNumber(number):
    for i in range(1, number + 1):
        print(i)

# showNumber(5)

# MINI PROJECT
# PRINT NUMBER FUNCTION

# def printNumber(number):
#     for i in range(1, number + 1):
#         return i

# Function that checks if a number is odd or even

def checkEvenOdd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

result = checkEvenOdd(51)

print(result)

# FIND THE SUM OF NUMBERS USING WHILE LOOP

def calculateSum(n):
    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1

    return total

result = calculateSum(10)
print(result)