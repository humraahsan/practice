# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint

easy_level = 10
hard_level = 5
turns = 0


def check_num(guess, num, turns):
    if guess > num:
        print("too high")
        return turns - 1
    elif guess < num:
        print("too low")
        return turns - 1
    else:
        print(f"You guessed it correct. The actual number was {num}")


def difficulty():
    level = input("Choose difficulty level. Type 'easy' or 'hard': \n")
    if difficulty == "easy":
        return easy_level
    else:
        return hard_level


def game():
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")
    num = randint(1, 100)
    print(f"The correct answer is {num}")

    attempts = difficulty()

    guess = 0
    while guess != num:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = float(input("Guess the number between 1 and 100: \n"))
        attempts = check_num(guess, num, attempts)
        if attempts == 0:
            print("You have run out of guesses, You lose!")
            return
        elif guess != num:
            print("Guess again")


game()
