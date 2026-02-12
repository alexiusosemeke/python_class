# Python OOP Concepts

# Encapsulation: This means bonding data and methods together and controlling access.
# This talks about hiding data such that you need to give someone access to have access to it
# Data hiding means keeping variable and the methods that work on the data inside one class and protecting the data from direct access
# DATA SHOULD NOT BE FREELY CHANGED FROM OUTSIDE THE CLASS

# Why:
# 1) Protect sensitive data
# 2) Prevent Invalid changes
# 3) Controls how data is modified
# 4) Makes code safe and cleaner





# INHERITANCE

class Animal:
    def __init__(self, name):
        self.name = name

# The Animal class is our parent class
# we will now create another class (child or sub class) and try to inherit properties and methods of the Animal class (parent class)

class Dog(Animal): # the Animal class is now being passed to the new Dog class.
    def __init__(self, name):
        super().__init__(name) # There'll be no need to use (self.name = name) since we already used super().__init__(name).



