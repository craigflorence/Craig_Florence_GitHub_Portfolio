# Lists are mutable, meaning they can be changed after their creation. Hence there are functions like append and pop to
# add or remove items from a list.

my_list = [1, 2.5, "Hello", True, False, ["a", "b", 1], (1, 2, 3)]
list2 = []
for item in my_list:
    list2.append(type(item))
print(list2)

# As you can see the list can hold different data types. You can use the .append() method to add new items to the end.

increasing = [1, 2, 3, 4, 5]
print(increasing)               # Output is [1, 2, 3, 4, 5]
increasing.reverse()
print(increasing)               # Output is [5, 4, 3, 2, 1]
decr = increasing.reverse()
print(decr)                     # Output is None
decreasing = increasing.copy()
decreasing.reverse()
print(decreasing)
decreasing = increasing[::-1]
print(decreasing)