total = 0
for student in range(1, 6):
    scores = float(input(f'enter the score for student{student} '))
    total += total + scores
avg = total/student
print(f'The average is {avg:,.2f}')
