# This is a simple guessing game where the player has to guess the sum of two hidden numbers.
# The player has 5 guesses to get the correct answer.

# Import necessary libraries
import random

# Initialize variables
score = 0
guesses = 0
rounds = 9

print("Welcome to the Mystery Sum Game!")
print("Guess the sum of two hidden numbers (1-10 each).")
print("You only get 5 guesses — try to score as high as you can!\n")

# Generate two random numbers between 1 and 10
# and calculate their sum
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
correct_answer = num1 + num2

# Start the guessing rounds
for round_num in range(1, rounds + 1):
    

    print(f"Round {round_num}: What is the sum of two secret numbers?")
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    guesses += 1

    if guess == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong.\n")

    if guesses == 5:
        print("You've used all 5 guesses!")
        break

print(f"\nGame Over! Your final score is: {score}/5")
print("Thanks for playing! Hope you had fun!")
print(f'If you were curious, the correct answer was: {correct_answer}')