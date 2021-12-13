for letter in "Craig":
    print(letter)
for number in range(7, 13):
    print(number)

friends = ["Kay", "Mitzi", "Dahlia"]

for index in range(len(friends)):
    print(friends[index])

# can loop through any collection of data

for index in range(10):
    if index == 0:
        print("First Iteration")
    elif 3 < index <= 6: # note here you can surround the variable with the
        print("Between 3 and 6")
    else:
        print("Other index")


def powerizer(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result


print(powerizer(2,3))


def to_tha_powa(base_num, indicie_num):
    power_iteration = 1
    val1 = base_num
    while power_iteration != indicie_num:
        val1 = val1 * base_num
        power_iteration += 1
    return val1

print(to_tha_powa(3,4))

# ---------------------------------------------- Nested For Loops -----------------------------------------------

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for array_top_level in number_grid:
    for array_inner_level in array_top_level:
        print(array_inner_level)


super_grid = [
    [
        [1], [2], [3]
    ]
]
for level_1 in super_grid:
    for level_2 in level_1:
        for level_3 in level_2:
            print(level_3)



# ----------------------------- A translator ----------------------------------

# Every vowel will be replaced with oo

def translate(to_translate):
    translation = ""
    for letter in to_translate:
        if letter in "AEIOUaeiou":
            if letter in "AEIOU":
                translation = translation + "Oo"
            elif letter in "aeiou":
                translation = translation + "oo"

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase to translate: ")))





