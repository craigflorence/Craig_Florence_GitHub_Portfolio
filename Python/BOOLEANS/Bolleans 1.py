# Boolean values only come in True or False

print(5 < 10)           # True that 5 is less than 10 so it displays True
print(5 == 3)           # False that 5 is equal to 3, so its False
print(3 != 1)           # True that 3 is not equal to 1 so it is True
print(not(5 == 5))      # False that 5 equals 5. 5 == 5 is True so it is False that 5==5 is False.
print("A bit more complicated:")
print(1 < 2 and 1 > 0)  # AND is TT = T TF,FT,FF = F 1 < 2 is T and 1 > 0 is T so AND TT = True
print(1 < 2 and 2 < 3 and 3 < 1)    # It goes T T F so it is False
print(1>0 or 1>5)