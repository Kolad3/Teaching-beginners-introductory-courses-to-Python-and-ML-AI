def show_menu():
    print('\nWhat can i help you with?')
    print('1. Greet me')
    print('2. Add two numbers')
    print('3. Tell me the time')
    print('4. Give me a fun fact')
    print('5. Exit')

def greet():
    name = input('what\'s your name?')
    print(f'hello, {name}! I hope you\'re doing well?')

def add_numbers():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(f'The sum of {a} and {b} is {a + b}')

def tell_time():
    from datetime import datetime 
    now = datetime.now()
    print('Current time is: ', now.strftime('%H:%M:%S'))

def fun_fact():
    import random
    facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren't.",
        "Octopuses have three hearts.",
        "A group of flamingos is called a 'flamboyance'."
    ]
    print('fun fact: ', random.choice(facts))

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