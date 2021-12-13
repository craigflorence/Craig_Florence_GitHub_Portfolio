# When writing code you get lots of red errors in the console that stop the program in its tracks, until you fix it
# but then you have to re-run it from the beginning.
# If you don't want the program to end with an error then you will have to try and capture the errors and handle them
# in a different way.

num1 = int(input("Enter a numerator: "))
num2 = int(input("Enter a denominator: "))

# print(num1/num2)

# in the above code if you make num2 = 0 then you divide by 0 which cannot be done.
# You see the red error ZeroDivisionError: division by zero
# If we not catch the ZeroDivisionError: division by zero error we can change the behaviour.

try:
    print(num1/num2)
except ZeroDivisionError:
    print("You cannot divide by zero")

