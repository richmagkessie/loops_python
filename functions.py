# This program defines and calls functions
# Function definition
name = input('Enter your first name ')
def main():
    # call in a function
    message()
    # print an end message

# another function
def message():
    # print username plus welcome message
    print('You\'re welcome', name)


main()
