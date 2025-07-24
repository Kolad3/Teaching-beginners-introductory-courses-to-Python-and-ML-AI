import random

print('Welcome to our Simple Random Game')

score = 0
for i in range(5):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = int(input(f'What is {num1} x {num2}?'))
    if answer == num1 * num2:
        print('Correct!')
        score+=1
    else: 
        print(f"wrong! The correct answer is {num1 *num2}")

print(f'Your total score is: {score}/5')
