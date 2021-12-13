# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# whether they guessed too low, too high, or exactly right.

from random import randint

number = randint(0, 9)
guess = 10  # Guess can't be 0, as the number could be 0 to begin with and the game would close immediately.
turn = 0

while guess != number and guess != "exit":
    guess = input("Guess: ")

    if guess == "exit":
        break

    while not type(guess) == int:
        try:
            guess = int(guess)
        except ValueError:
            print("Needs to be a number 0-9")
            guess = input("Try again: ")
    turn += 1

    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low!")
    else:
        print("Well done!")

    again = input("Play again? Y/N ")
    if again == "N" or again == "exit":
        break
        if again == "Y":
            guess = ""
            turn = 0
            number = randint(0, 9)

        while again != "Y" and again != "N" and again != "exit":
            again = input("Y or N")
            if again == "N" or again == "exit":
                break
            if again == "Y":
                guess = ""
                turn = 0
                number = randint(0, 9)
            guess = 0
            turn = 0
            number = randint(0, 9)

