# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 

# First just try to successfully generate a fibonacci sequence.

# fib_start = [0, 1]
# for i in range(1):
#     a = fib_start[-1] + fib_start[-2]
#     fib_start.append(a)
# print(fib_start)

# Now make it a function and ask for input

def fibonacci():
    """ Returns n values of the fibonacci sequence."""
    status = True
    while status:
        fib_start = [0, 1]
        n = input(">>>>: ")
        if n == "q":
            status = False
            break
        try:
            r = int(n)
        except ValueError:
            print("Type a number or q to quit")
        if r == 0:
            print([0])
        elif r == 1:
            print([0, 1])
        else:
            for i in range(n):
                a = fib_start[-1] + fib_start[-2]
                fib_start.append(a)
        print(fib_start)
fibonacci()