eg_list = [1, 2, 3, 4, 5]
print(eg_list)
while eg_list:
    print(eg_list.pop(-1))
    print(eg_list)
print(eg_list)

# *************************************************************************************************************

messy_list_1 = ["Gandalf", 2, "Bilbo", 4, "Gimli", "Sauron", 3, 1]
messy_list_2 = [5, 8, "Legolas", 6, 7, "Golem", 9, "The Shire", 10]

clean_names = [n for n in messy_list_1 + messy_list_2 if type(n) == str]
print(clean_names)
clean_numbers = sorted([n for n in messy_list_1 + messy_list_2 if type(n) == int])
print(clean_numbers)

# ***********************************************************************************************************

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