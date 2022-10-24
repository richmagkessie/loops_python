# Christiana owns an import business, she wants to know how much she sell her products at a retail price
# retail_price = wholesale_price * 2.5

mark_up_percentage = 2.5 # The multiplying factor
another_item = 'y'        # This would control the loop

# Process one or more items
while another_item == 'y':
    # get the wholesale_price of the item
    wholesale_price = float(input('Enter the wholesale price of the item: '))

    # Calculate the retail_price
    retail_price = wholesale_price * mark_up_percentage

    # Display the retail Price
    print(f'Retail Price: ${retail_price:,.2f}')

    # Do this again?
    another_item = input('Do you have any more item?' + 'Enter y for yes: ')
