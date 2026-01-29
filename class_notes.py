# Tuples: Tuples are a built-in python data structure used to store multiple items in a single variable, similar to a list but with one key difference: They are immutable (meaning they don't change)

# Characteristics of Tuple
# 1: Ordered
# 2: immutable
# 3: Allows duplicate value
# 4: Written with parenthesis

# Why Tuple?

# Data should not be changed. Easy to access faster than List. Used for fixed record (e.g. Coordinates, data record)

# student = ("John", 17, "Python")
# print(student[-2])

# numbers = (1, 1, 12, 3 , 3,2,3,4,5)
#print(numbers.count(1)) # This checks for the number of occurrencies of that particular number in our tuple
#print(numbers.index(2)) # This checks for the index location (where the number is located in our tuple).

names = ("Segun", "Femi", "Emmanuel", "Femi", "Precious")
print(names.index("Femi"))
print('---------')

# Use tuple to create a student record, display each of the information neatly

record = ("Segun", 18, "Python",)
print(record[0])
print('---------')
name, age, course = record
print(name)
print(age)
print(course)

print('---------')

# Set
# A set is an unordered, mutable collection of unique items
# A set is unique, meaning it cannot contain

# Characteristics
#1: No duplicate values -> Using duplicate values might lead to loss of data
#2: Unordered -> Meaning there's no index
# 3: Written using curly braces {}
# 4: Fast membership checking

myfirstset = {1, 2, 3, 3}
print(myfirstset)

print('------------')

# Dictionary
# Dictionary is the most unique of them all.  A dictionary is a list like structure that holds key value pairs. It stores data as key-value pairs

# Characteristics
# 1: Key must be unique
# 2: Values can be anything
# 3: They are mutable
# 4: Written using {key: value}
# 5: Fast data lookup. We don't use index to search for values, instead we use the key

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("brand")
print(thisdict) #This prints everything in the dictionary
# print(thisdict.get("brand")) # This gets the value of the brand key
# print(thisdict["model"]) # This also gets the value of the model
for key, value in thisdict.items():
    print(f"{key}: {value}")

# Mini Project: Student Management System

# 1: Store student's details
# 2: Display them neatly
