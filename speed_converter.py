# This program converts the speeds from kph to mph
start_speed = 0
conversion_factor = 0.6214
print('You\'re converting a range of speed from 0 to a speed you choose(from kph to mph)')
end_speed = int(input('Enter end speed: '))

# Print table heading
print('KPH\tMPH')
print('------------------------')

# Print speeds using for loops
for kph in range(0, end_speed):
    mph = kph * conversion_factor
    print(f'{kph}\t{mph}')
