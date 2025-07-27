# This code implements a simple mini assistant that can greet the user, add two numbers, tell the current time, and provide a fun fact.
# It uses a menu-driven approach to allow the user to choose an action, and it runs in a loop until the user decides to exit.

from datetime import datetime 
import random

# This function displays the menu options to the user.
# It provides a list of actions that the user can choose from.
def show_menu():
    print('\nWhat can i help you with?')
    print('1. Greet me')
    print('2. Add two numbers')
    print('3. Tell me the time')
    print('4. Give me a fun fact')
    print('5. Exit')

# This function handles the greeting action.
# It prompts the user for their name and prints a greeting message.
def greet():
    name = input('what\'s your name?')
    print(f'hello, {name}! I hope you\'re doing well?')

# This function handles the addition of two numbers.
# It prompts the user for two numbers, adds them, and prints the result.
def add_numbers():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(f'The sum of {a} and {b} is {a + b}')

# This function tells the current time.
# It uses the datetime module to get the current time and formats it for display.
def tell_time():
    now = datetime.now()
    print('Current time is: ', now.strftime('%H:%M:%S'))

# This function provides a random fun fact.
# It selects a randomfact from a predefined list and prints it.
def fun_fact():
    facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren't.",
        "Octopuses have three hearts.",
        "A group of flamingos is called a 'flamboyance'."
    ]
    print('fun fact: ', random.choice(facts))

# Main loop to run the mini assistant
# It displays the menu, takes user input, and calls the appropriate function based on the user's choice.
print('Welcome to the Mini Assistant!')
while True: 
    show_menu()
    choice = input('Enter your choice (1-5): ')
    if choice == '1':
        greet()
    elif choice == '2':
        add_numbers()
    elif choice == '3':
        tell_time()
    elif choice == '4':
        fun_fact()
    elif choice == '5':
        print('Goodbye and have a lovely day')
        break
    else:
        print('Invalid choice, please try again.')