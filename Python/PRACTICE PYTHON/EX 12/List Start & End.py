# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new 
# list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

from random import randint
numbers = [randint(1,100) for i in range(10)]


def end_start(listt):       # In this version there are two sub-variables.
    a = listt[0]
    b = listt[len(listt)-1]
    new_list = [a , b]
    return new_list


def start_end(list):        # I managed to turn it into a list comprehension.
    new_list = [list[0], list[len(list)-1]]
    return new_list

print(f"Start_end: {start_end(numbers)}")
print(f"end_Start: {end_start(numbers)}")
