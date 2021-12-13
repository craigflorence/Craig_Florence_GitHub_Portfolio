friends = ["Kern", "Mitzi", "Dahlia"]
ages = [25, 26, 27]
# You can use index values in square brackets to pull a single list value. Or a range of list values.
# If you count back from the end, you start at -1, then -2 etc.

print(ages)
print(friends[2])
print(friends[-1])
print(friends[0:2])

# You can then change the value of any list member by referring to the index position.

friends[1] = "MITZI"

print(friends)

# ---------------------------------------- Using list functions ----------------------------

lucky_numbers = [1, 6, 9, 3, 5, 7, 2]
people = ["Jon", "Tim", "Sen", "Kim", "Ron", "Lii", "Lon"]

people.extend(lucky_numbers)
print(people)

lucky_numbers = [1, 6, 9, 3, 5, 7, 2]
people = ["Jon", "Tim", "Sen", "Kim", "Ron", "Lii", "Lon"]

# Above error about list literal is saying don't define a list, then immediately change it. Just add the changes from
# the beginning.

# Append adds to the end of the list.
# Insert will insert to the given index position.
# Remove deletes the matched list item, so spell it correctly.
# Clear will remove everything from the list, leaving it empty.

people.append("Ivan")
print(people)
people.insert(2, "Jay")
print(people)
people.remove("Sen")
print(people)
people.clear()
print(people)

# Pop will remove an item from the list, and you can specify the index.

people = ["Jon", "Tim", "Sen", "Kim", "Ron", "Lii", "Lon"]
people.pop()
print(people)
people.pop(3)
print(people)

# Index will return the start index of the matched list item.

print(people.index("Lii"))

# You can count how many times something appears in the list.
# You can use sort to order items in a list.
# You can reverse the order of a list.
# You can copy a list to another using copy.

numbers = [1, 5, 7, 9, 1, 2, 3, 1, 5]
print(numbers.count(1))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# GOOD EXAMPLE -----------------!!!-----------------!!!------------------!!!----------------------!!!
# I wanted to get the ascending list, copy it to a temp list and then reverse the temp one to get a descending list.
# Meaning I had an intact ascending list. However the result was None, as the .reverse function does an in-place
# reverse, meaning that you have to split it out into separate lines.

numbers_ascending = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers_ascending)                            # Gives the list 1-9
numbers_temp = numbers_ascending.copy()             # Copies list to _temp
print(numbers_temp)                                 # Prints list 1-9
numbers_temp.reverse()                              # _temp is now reversed
print(numbers_temp)                                 # Prints 9-1
numbers_descending = numbers_temp                   # New list name
print(numbers_descending)                           # Prints 9-1

numbers_descending = list(reversed(numbers_ascending))      # Use the reversed function, instead. Or split it up.
print(numbers_descending)

#---------------------------------- TUPLES ---------------------------------------------------------------------
# a tuple stores different information.

coordinates = (4, 5) # a tuple with coordinates inside it. It is IMMUTABLE - it cannot be changed or modified.
# IMMUTABLE means that no functions like the above in LISTS will affect it.
print(coordinates[1]) # this will print 5

# Tuples vs Lists - a list that cannot be changed after being created. Use Tuples for data that will never change.
# You can create a LIST of TUPLES
coordinates2 = [(4,5), (6,7), (8,9)]
