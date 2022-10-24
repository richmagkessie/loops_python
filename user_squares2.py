# This program squares numbers
# It uses a loop to display a table of numbers and their squares

# Get the start value
print('This program prints a list of numbers and their squares.')
start = int(input('Enter the starting number: '))

# Get the end value
end = int(input('Enter the end value: '))

# Print the table headings
print('\n')
print('Numbers\tSquare')
print('----------------')

# Print numbers and their squares
for numb in range(start, end+1):
    square = numb ** 2
    print(f'{numb}\t{square}')
