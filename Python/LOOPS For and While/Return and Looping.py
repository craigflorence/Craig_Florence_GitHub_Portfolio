#  A function is a collection of code that performs a specific task. Sometimes you want the function to run a task,
#  then return some value back.
#  the return keyword does this

def cubify(number):
    number*number*number

print(cubify(3)) # This comes back as None so we need the return the value

def cube(number):
    return number*number*number
    print("Hello you can't see me!") #  the return keyword breaks the function at that point so it will stop
    # processing further code.

print(cube(3))
# or
value = cube(3)
print(value)

# ------------------------------------------ IF statements -------------------------------------------------

is_male = False

if is_male:  # in this example the IF statement will always assume = True, so you don't need to specify it.
    print("They are male")
else:
    print("Probably female")

is_woman = True

if is_woman == False:
    print("Not woman")
else:
    print("Woman!")

# the NOT() function negates whatever is passed into it. So by defult if is_tall looks for a True value.

is_child = True
is_female = False

if is_child and is_female:
    print("Its a little girl")
elif is_child and not is_female:
    print("It's a little boy")
elif not is_child and is_female:
    print("Its a woman")
elif not is_child and not is_female:  # I used elif to the end instead of else to show double not() works too
    print("It's a man or alien!")

# ------------------------- Operators using IF

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num1 and num2>= num3:
        print(num2)
    else:
        print(num3)
max_num(5,5,3)

def max_num_list(a, b ,c ):
    list1 = [a, b, c]
    print(max(list1))
max_num_list(5,5,3)

# above are 2 ways of the same thing - but one using ifs and operators.
# operators include > < >= <= == !=

