# Use strings, file handling, and error handling to store and retrieve students data

# Requirements:
# ask user for:
                # - Student name
                # - Age
                # - Course

# Save details to a files
# Read all saved records
# Handle:
#         - Invalid inputs
#         - Missing file


try:
    studentName = str(input('Enter student name: ')).strip()
    studentAge = int(input('Enter student age: '))
    studentCourse = str(input('Enter student course: ')).strip()

    with open('students.txt', 'a') as file:
        file.write(f"Student Name: {studentName} \n")
        file.write(f"Student Age: {studentAge} \n")
        file.write(f"Student Course: {studentCourse}\n\n\n")
        print('Student data saved successfully')
except ValueError as error:
    print('Error', error)
except Exception as e:
    print('An error occurred', e)
else:
    print('Data processing completed')
finally:
    print('THANK YOU FOR BANKING WITH US. ')




# Complete the class code to stand the following test:
# Prevent empty names
# Add option to view all students
# Format output neatly
# Add menu: (Add student, View Students)
