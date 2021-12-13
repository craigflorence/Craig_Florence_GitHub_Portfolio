# For loops are used to iterate through a series of items and do something with them.

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for trio_of_numbers in number_grid:
    for individual_number in trio_of_numbers:
        print(individual_number)


# The above code is taking the first list of numbers [1, 2, 3] and storing it all inside the variable trio_of_numbers.
# Then, inside the first trio_of_numbers it is storing the first number, 1 in the variable individual_number. It then
# prints this to the console and starts again moving  on to list 1 [1 ,2 3] number 2. Then list 1 number 3 is 3. Then it
# goes to list 2 [4, 5, 6] and does the same, and for list 3 [7, 8, 9].

advanced_grid = [# think of this as layer 1
    [# this is layer 2
        [# and layer 3 has the lists inside it
            ["a", "b", "c"],
            ["d", "e", "f"]
        ]
    ]
]

for contents_layer_1 in advanced_grid:
    print("Layer 1 includes: " + str(contents_layer_1))
    for contents_layer_2 in contents_layer_1:
        print("Layer 2 includes: " + str(contents_layer_2))
        for contents_layer_3 in contents_layer_2:
            print("Layer 3 includes: " + str(contents_layer_3))
            for letters in contents_layer_3:
                print(letters)

