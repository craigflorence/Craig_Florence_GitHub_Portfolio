# How to deal with ending/completing a loop and how to break out of a loop.

number_of_attempts = 5
connection_status = False
count = 0

for attempts in range(0, number_of_attempts):
    count += 1
    print(f"Attempting to connect {count} of 5.")
    if connection_status:
        print("Connected.")
        break
else:
    print("Unable to connect.")
