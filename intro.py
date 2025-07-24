print("Hello World")

'''
name = 'Kolade'
age = 60
height = 6.5
is_student = True
list = [1, 2, 3, 4, 5]
'''

'''
name = input('What is your name?)
print('Nice to meet you, ' + name)

'''

'''
age = int(input('What is your age? '))
if age >= 18:
    print('You are an adult.')
else:
    print('You are still young.')

'''



'''
Operators in Python
Operators are symbols that perform operations on variables and values. 

***Arithmetic Operators: Perform mathematical calculations (+, -, *, /, %, **, //).

***Comparison (Relational) Operators: Compare values and return a boolean result (==, !=, <, >, <=, >=).

***Assignment Operators: Assign values to variables (=, +=, -=, *=, /=, etc.).

***Logical Operators: Combine conditional statements (and, or, not).

***Identity Operators: Check if two variables refer to the same object (is, is not).

***Membership Operators: Check if a value is present in a sequence (in, not in).

***Bitwise Operators: Perform operations on individual bits of numbers (&, |, ^, ~, <<, >>).

'''

'''
import random
number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct!")
else:
    print("Wrong! The number was", number)

'''
for i in range(5):
    print("Hello", i)

count = 0
while count < 5:
    print("Hi", count)
    count += 1

def greet(name):
    print("Hello", name)

greet("Kolade")