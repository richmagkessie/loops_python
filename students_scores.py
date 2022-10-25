# This program calculates the average score of all students
# Get the number of students in the class
num_of_students = int(input('Enter the number of students: '))

# Loop to get the students course
for student in range(1, num_of_students + 1):
    # Get the number of courses
    num_of_courses = int(input(f'Enter the number of courses for student {student} '))
    for course in range(1, num_of_courses + 1):
        course_score = float(input(f'Enter scores for course {course} '))
        total = 0
        total += total + course_score
    avg_score = total/num_of_courses
print('==============================')
print(f'Student\t\tAverage')
print('==============================')
print(f'Student{student}\t{avg_score:,.2f}')
