import os
import random

def main():
    print("""
    Welcome to CLI Guess the Number!
    You have 3 diffuculty options to select.
    ====================================================
    (e)asy
    (m)edium
    (h)ard
    ====================================================
    Please select your difficulty level by typing 'e', 'm', or 'h'.
    """)
    difficulty = input("> ").lower()

    if difficulty == "e":
        minint = 10
        maxint = 100
        number = random.randint(10,100)
    elif difficulty == "m":
        minint = 10
        maxint = 999
        number = random.randint(10,999)
    elif difficulty == "h":
        minint = 10
        maxint = 9999
        number = random.randint(10,9999)
    else:
        print("Invalid input. Please try again.")
        main()

    print("I am thinking of a number between " + str(minint) + " and " + str(maxint))
    print("You have as many chances as you need to guess the number.")

    print("When you're ready, enter your first guess.")

    guesses = int(1)

    guess = int(input("> "))

    while guess != number:
        guesses = int(guesses) + 1
        if guess > number:
            print("The actual number is lower than your guess!")
            guess = int(input("> "))
        elif guess < number:
            print("The actual number is higher than your guess!")
            guess = int(input("> "))
    
    print("Well done! The answer was " + str(number) + "! It took you " + str(guesses) + " attempts to get the correct answer.")

main()