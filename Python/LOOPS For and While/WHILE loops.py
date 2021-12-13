i = 1
while i <= 5:
    print(i)
    i += 1
print("Now more than 5")


def f(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("You can't divide by 0")

print(f(5,0))

def guessing_game(secret_word, number_of_attempts):

    """guessing_game(...)
                        guessing_game(secret word [, number_of_attempts])

    Give the function a secret word and specify the number of attempts.
    The word must be given and number of attempts defaults to 2"""

    secret_word_game = secret_word.upper()
    attempts = 0
    guess_status = True
    guess_user = ""
    try:
        while secret_word_game != guess_user and guess_status:

            if attempts <= number_of_attempts:
                 attempts += 1
                 guess_user = input("Guess the word: ").upper()
            else:
                 guess_status = False
            if not guess_status:
                print("You didn't guess in time.")
            else:
                 print("Well done!")

    except TypeError:
                    print("You must give a word to guess when calling the function")

guessing_game(hello,number_of_attempts=2)