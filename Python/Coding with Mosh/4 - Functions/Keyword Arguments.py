def increment(number, by):
    return number + by


print(increment(2, by=5)) 
# You can specify the keyword, parameter, of the argument to improve readability.
# You can also set parameters to defulat argument if nothing is passed to the function when called

def increment_v2(number, by=1):
    return number + by

print(increment_v2(10, 5))