# Mini Project: Student Management System

# 1: Store student's details
# 2: Display them neatly

studentsData = {
    '1': {
    'first_name': 'John',
    'last_name': 'Smith',
    'email': '',
    'age': 22,
    'subjects': {
        'Mathematics',
        'Physics',
        'Chemistry',
    },
    'has_paid_fees': True,
},
}

# print(studentsData) #This is to print all the data in the dictionary
# for key, value in studentsData.items():
#     print(f"{key}: {value}")

for x, obj in studentsData.items(): # here we loop through the first
    print(x)

    for y in obj:
        print(y)

