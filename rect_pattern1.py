# Printing some shapes with loops

# Triangular
print('Triangular Shape\n--------------------------')
for row in range(6):
    for col in range(row+1):
        print('*', end='')
    print()


# Rectangular shape
print('\n------------------\nRectangular Shape')
for row in range(5):
    for col in range(10):
        print('*', end='')
    print()

# Inverted Triangle
# that is reverse for loop
print('\n----------------\nInverted triangle')
rows = 8
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print('*', end='')
    print()
