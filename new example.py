'''
name = ['kolade','samuel', 'daniel']
#  age = 60
height = 6.5

print('My name is ', name[2] ) 

name = input('what is your name? ')

print(' hi ', name)


age  = int(input("what's your age?"))

if age >= 16 and age <= 18: 
    print('You belong to the super teens')
elif age >= 13 and age <= 15:
    print('You belong with the junior teens')
else: 
    print('You do not belong to any of the categories, ' \
    'please meet the coordinators to assist you further')
    
'''
'''
for i in range(10):
    print ('Hello', i)


def greet(name):
    print('hello', name)

greet('kolade')
'''
count = 0
while count < 5:
    print ('Hi', count+1)
    count += 1
