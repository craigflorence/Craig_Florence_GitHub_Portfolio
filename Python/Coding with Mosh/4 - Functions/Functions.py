# first_name and last_name in the function are called PARAMETERS
# but when you assign a value to the PARAMETER they are called arguments
# def function(parameter1, parameter2) function(argument1, argument2)

def greet(first_name, last_name): 
    print(f"Hi there! {first_name} {last_name}")
    print("Welcome!")


greet("Craig", "Florence") # This is calling the function. # Craig and Florence are arguments

# Functions can do one of two things:
# 1 - Perform a task
# 2 - Return a value

# Above the greet() function performs the task of print() a string.
# Below the greet_v2() function returns a value.

def greet_v2(f, l):
    return f"Name: {f} {l}"
greet_v2("John", "Doe")
name = greet_v2("John", "Doe")
print(name)
# Returning a value can be used for storing the result in another variable for future use.
# message = greet_v2("Craig", "Florence") is an example of storing a returned function value.

# If you call greet() you will get None
# If you call greet_v2() you will get Name: Craig Florence - v2 can also be assigned to a variable

