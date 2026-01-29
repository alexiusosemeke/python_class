#Strings in Python

#sequence of characters enclosed in a single quote, double quotes, or triple quotes

# text1 = ' hello'
# print(text1.strip())
text2 = 'This is just a text'
# print(text2.replace('text', 'message'))
# print(text1.isalpha())


# FILE HANDLING IN PYTHON

# File handling allows python to read from and write to file on your system

# HOW TO OPEN A FILE IN PYTHON

# r -> read
# w -> write
# a -> append
# x -> to create a file
# rb -> Read binary

# Best Practices
# making use of 'with'

file = open('text.txt', 'r')
# with open('text.txt', 'w') as file:
#     file.write(text2)

with open('text.txt', 'r') as file:
    content = file.read()
    print(content)
# with open('text.txt', 'r') as file:
#     contents = file.read()
#     print(contents)
#     file.write(text2)

#APPENDING TO A FILE

# This is the same thing as writing to a file, only difference is that we'll change the 'w' to 'a'



# TRY CATCH AND EXCEPTION BLOCK