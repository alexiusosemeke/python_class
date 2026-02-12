# OOP -> A programming approach that organises code into classes and objects, making programs easier to manage, reuse, and understand
# why:
#  - organises large programs
#  - reuses code
#  - models real-world objects
#  - easier to maintain

# CLASS is a blueprint or template for creating objects
# OBJECT is an instance of a class

# Real life example

# class -> car
# Object -> Toyota, Mercedes, Honda

# THE __init__ METHOD CONSTRUCTOR
# __init__ is a special method that runs automatically when an object is created



class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

Alex = Person('Alex', 30)