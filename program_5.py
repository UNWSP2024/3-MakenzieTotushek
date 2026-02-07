# Author: Makenzie Totushek
# Date: 2/6/2026
# Title: Hot Dog Price

# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

#Get the kind of Hot Dog
hotdog_type = input('Please enter the kind of hot dog: ')
if hotdog_type == 'Hot Dog' or hotdog_type == 'hot dog':
    print('The price of the Hot Dog is $3.50')
    hotdog_type = float(3.50)
else:
    print('The price of the Chili Dog is $4.50')
    hotdog_type = float(4.50)

#Ask about cheese
cheese_topping = input('Would you like cheese for $0.50? (Y/N) ')
if cheese_topping == 'Y' or cheese_topping == 'y':
    cheese_topping = float(0.50)
else:
    cheese_topping = float(0.00)

#Ask about peppers
pepper_topping = input('Would you like peppers for $0.75? (Y/N) ')
if pepper_topping == 'Y' or pepper_topping == 'y':
    pepper_topping = float(0.75)
else:
    pepper_topping = float(0.00)

#Ask about onions
onion_topping = input('Would you like grilled onions for $1.00? (Y/N) ')
if onion_topping == 'Y' or onion_topping == 'y':
    onion_topping = float(1.00)
else:
    onion_topping = float(0.00)

#Display total
subtotal_price = float(hotdog_type + cheese_topping + pepper_topping + onion_topping)
print(f'Subtotal: {subtotal_price}')
tax = float(subtotal_price * 0.07)
print(f'Tax: {tax:.2f}')
total_price = float(subtotal_price + tax)
print(f'Total: {total_price:.2f}')