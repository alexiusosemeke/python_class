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

showNumber(5)