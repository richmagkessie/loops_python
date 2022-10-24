# This program averages the scores of students

# Get the number of students
num_of_students = int(input('Enter the number of students whose test scores are to be averaged: '))

#sum
total = 0
# loop to get scores of students
for student in range(1, num_of_students+1):
    #get scores for courses for the student
    num_of_courses = int(input(f'Enter number of courses for student {student}: '))
    for course in range(1, num_of_courses+1):
        course_score = float(input(f'Enter score for course {course}: '))
        total += total + course_score

    # finding nAvgScore
    avgScore = total/num_of_courses
    # print student plus average score
    # print table headings
    print()
    print('Student\t\tAvgScore')
    print('-------------------------------')
    print(f'Student{student}\t{avgScore:,.2f}')
