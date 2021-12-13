# Variables are containers for data.

character_name = "Assad"
character_age = "19"
story = "There was a person called " + character_name + " who was a mischievous " + character_age + "-year-old."
print(story)

# In the above, note the following:
#       1) Age is a string, not an integer for ease of adding it in-line to the story. Otherwise you would have to
#       convert it from integer to String.
#       2) Each section of the string is in " " and then the variable is surrounded by + signs.

# ------------------------------------------------------------------------------------------------------------- #

# The data types are Strings, Numbers and Booleans - The main 3
# Strings are plain text. \n means new line. \ will escape the next character.
# Integers are whole numbers
# Floats are decimal numbers
# Boolean means True or False

# -----------------------------------------   STRINGS  --------------------------------------------------------
user_name = "Craig"
user_age = 17
entry_req = False
print("Hello")
print("Hello\"")

# Tools like .lower and .upper convert strings to lower or upper case. Make sure to use the second set of ()!

my_sentence = "Hello! My name is Craig"
print(my_sentence)
print(my_sentence.upper())
print(my_sentence.lower())

# .isupper and .islower return a boolean value if a string is sully upper or lower case. Try them back to back.

my_upper = "HELLO"
my_lower = "hello"
my_mixed = "HeLlO"

print(my_lower.islower())
print(my_mixed.islower())

print(my_lower.upper().isupper())

# The LEN() function is useful for finding the length of a string.

my_password = "h456j5eyNTThu6jhwty5u6thr65yut4yu6rhty6htwtytjhyrethgythyutrjfghurykfju6irkyju6irkyrju56rjt"
print(len(my_password))

# Indexing refers to starting from 0 at the far left, and counting up characters from there.
# You refer to an index by using [ ] square brackets. How do we extract only Huffer?
# 0 1   2   3   4   5   6   7   8   9 10    11  12  13  14  15  16 ...
# F L   O   R   E   N   C   E   ,   H  U     F   F   E   R   ,   C ...

data_dump = "Florence,Huffer,Craig,Spain,Coin"
print(data_dump[9:15])
# Remember that 9 is inclusive, but 15 is exclusive, meaning 9 is included. 15 means the one before it.
# The index function .index will find the index for you.

print(data_dump.index("Huffer"))
# It returns 9, saying it starts at index 9.

# the . replace function can be used to replace part of a string.
print(data_dump.replace("Spain", "Espana"))
spain = "spain SPAIN spain spain"
print(spain.replace("spain", "ES", 2))

# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------- NUMBERS --------------------------------------------------------------
# % Mean modulus - or the remainder of a division. 10/3 is 3 r1 so 10%3 shows 1. 11/3 = 3 r 2 so 11%3 shows 2
# All division end up with a decimal point.

print(2)
print(2.0987)
print(-4.9)
print(1 + 2)
print(3.4 + -2.3)
print(4 * 4)
print(10 / 5)
print(10 % 3)
print(11 % 3)
print(10 / 3)

# You cannot print a string and include an integer, You have to convert the Int to Str with the Str() function.

age = 18
print("I am this age: " + str(age))

# abs returns the ABSOLUTE value of a number.
negative_number = -78
print(abs(negative_number))

# pow lets you use a power, exponent.
print(pow(7, 5))

# max and min will return the highest and lowest values.
scores = 1, 4, 9, 4, 5, 2
print(max(scores))
print(min(scores))

# 10 / 3 gives a recurring decimal 3.333333 - To round it up use round() function
sum = 10 / 3
print(round(sum))
round_up = 5.8
print(round(round_up))

# ---------- Not everything is included in Python to begin with. You may need to IMPORT a module.
from math import *
print(sqrt(64))
