# Write a program that will write even numbers to the console.

number_of_numbers = 90
counter = 0
for nums in range(1, number_of_numbers):
    if nums % 2 == 0:
        print(nums)
        counter += 1

print(f"There are {counter} evens.")
