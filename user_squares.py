# This program squares numbers
# It uses a loop to display a table of numbers and their squares

# Get the ending limit
print('This program displays a list of numbers (starting at 1) and their sqaures')
end = int(input('How far should the program go? '))

# Print the headings of the table
print('\n')
print('Number\tSquare')
print('--------------')

# Print the numbers and their squares
for number in range(0, end+1):
    square = number ** 2
    print(f'{number}\t{square}')
