# When using multiple conditions in one statement, you can group 
# them with brackets.

good_credit = 0
high_income = 0
student = True

message = "Elegible" if ((high_income or good_credit) and student) else "NA"

print(message)
print(type(good_credit))