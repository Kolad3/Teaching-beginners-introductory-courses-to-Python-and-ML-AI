def show_menu():
    print("\n Hello and what can i help you with today?"
          "\n 1. Greet me" 
          "\n 2. Add two numbers"
          "\n 3. tell me the time"
          "\n 4. Tell me a fun fact"
          "\n 5. Exit")
    '''
    print('1. Greet me')
    print('2. Add two numbers')
    print('3. tell me the time')
    print('4. Tell me a fun fact')
    print('5. Exit')
''' 
def greet():
    name = input("What's your name: ")
    print(f"Hello, {name}! I hope you're doing well?")

def add_two_numbers():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print(f'The sum of {num1} and {num2} is {num1 + num2}')

def tell_time():
    from datetime import datetime
    now = datetime.now()
    print("Current time is: ", now.strftime('%H:%M:%S'))    
    
def fun_fact(): 
    import random 
    facts = [
        'Honey never spoils',
        'Bananas are berries, but strawberries arent', 
        'Octopuses have three hearts.',
        'A group of Flamingos is called a flamboyance.'
    ]
    print('fun fact: ', random.choice(facts))

while True: 
    show_menu()
    choice = input('Enter number from 1-5: ')
    if choice == '1':
        greet()
    elif choice == '2':
        add_two_numbers()
    elif choice == '3':
        tell_time()
    elif choice == '4':
        fun_fact()
    elif choice == '5':
        print('Goodbye and have a lovely day!')
        break
    else: 
        print('Invalid choice, please try again.')