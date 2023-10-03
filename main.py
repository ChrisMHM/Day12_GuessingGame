import art 
import random

randomNumber = random.randint(1, 100)
attempts = 0
again = True
guess = 0

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

print(f"Pssst, the correct answer is {randomNumber}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5


while again:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > randomNumber:
        print("Too high.")
        again = True
    elif guess < randomNumber:
        print("Too low.")    
        again = True
    else:
        print(f"You got it! The answer was {guess}.")
        again = False
    attempts -= 1
    if attempts == 0 and again == True:
        again = False
        print("You've run out of guesses, you lose.")
    elif again == True:
        print("Guess again.")

