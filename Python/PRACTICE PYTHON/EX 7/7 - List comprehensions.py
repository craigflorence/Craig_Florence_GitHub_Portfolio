# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python
# that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

evens = [i for i in a if i % 2 == 0]
print(evens)

# The idea of a list comprehension is to make code more compact to accomplish tasks involving lists.
# Take for example this code:
#
#   years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
#   ages = []
#   for year in years_of_birth:
#     ages.append(2014 - year)

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2021 - year for year in years_of_birth]
print(ages)