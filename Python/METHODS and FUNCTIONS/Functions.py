# A function is a chunk of code that performs a specific task.
# A function that says Hi to the end user

def say_hi():  # all the code that comes after this line will be inside this function
    print("Hello to you!")


# now you must call the function

say_hi()


# you can pass information into a function - Parameters

def say_name(name, surname):
    print("Hello " + name + " " + surname)


say_name("Craig", "Florence")


def nonsense(num1, num2, word1, word2):
    number = int(num1) + int(num2)
    words = word1[:num1] + word2[num2:]
    output = words + str(number)
    print(output)


nonsense(1, 3, "blue", "orange")


# -------------------------------------------------------- Guessing Game ----------------------------------------------

def guessing_game(word_to_guess, number_of_guesses=3):
    """This is a guessing game. Enter a word to guess and how many attempts you want. The default is 3"""
    word_to_guess_game = word_to_guess
    user_guess = ""
    number_of_attempts = 1
    max_attempts = number_of_guesses
    game_status = True

    while user_guess.upper() != word_to_guess_game.upper() and game_status:
        if number_of_attempts < max_attempts:
            user_guess = input("Guess: ")
            number_of_attempts += 1
            if number_of_guesses-number_of_attempts == 1:
                print("You only have " + str(number_of_guesses-number_of_attempts) + " guess left")
            elif number_of_guesses-number_of_attempts == 0:
                print("Out of guesses!")
            else:
                print("You have " + str(number_of_guesses-number_of_attempts) + " guesses left!")
        else:
            game_status = False
    if not game_status:
        print("Failure")
    else:
        print("Winner!")


guessing_game("hey", 5)
print(help(guessing_game("hey")))