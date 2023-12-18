# Dictionary representing a student's information
student_info = {
    'name': 'Alice',
    'grades': [90, 85, 92, 88],
    'courses': ['Math', 'History', 'Science', 'English']
}

# Accessing the 'courses' list from the dictionary
student_courses = student_info['courses']

# Accessing specific data from the 'courses' list
first_course = student_courses[0]
second_course = student_courses[1]

# Printing the accessed data
print("Student Courses:", student_courses)
print("First Course:", first_course)
print("Second Course:", second_course)
