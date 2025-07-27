
list_of_names = ['kolade','samuel', 'daniel']    # This snippet creates a list of names and demonstrates how to assign values (lists) to variables in Python
age = 60                                         # This snippet assigns an integer value to a variable in Python
height = 6.5                                     # This snippet assigns a float value to a variable in Python

print('My name is ', list_of_names[2] )          # This snippet prints the name at index 2 from the list

name = input('what is your name? ')              # This snippet takes user input for their name, it demonstrates how to use input in Python

print(' hi ', name)                              # This snippet prints a greeting message with the user's name it has taken as input




# A simple snippet of code to demonstrate how conditional statements work in Python

# This code checks the age of a person and categorizes them into different teen groups.

age  = int(input("what's your age?"))


if age >= 16 and age <= 18: 
    print('You belong to the super teens')

elif age >= 13 and age <= 15:
    print('You belong with the junior teens')

else: 
    print('You do not belong to any of the categories, ' \
    'please meet the coordinators to assist you further')
    



# This snippet demonstrates a simple loop in Python that prints "Hi" five times.
count = 0
while count < 5:
    print ('Hi', count+1)
    count += 1

# This is another snippet that demonstrates a simple for loop in Python that prints "Hello" followed by the index number.
for i in range(10):
    print ('Hello', i)


# This snippet demonstrates how to define a function in Python and call it.
def greet(name):
    print('hello', name)

greet('kolade')