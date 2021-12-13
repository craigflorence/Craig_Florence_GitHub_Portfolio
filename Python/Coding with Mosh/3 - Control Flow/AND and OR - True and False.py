# The AND logical operator will evaluate until it finds a FALSE statement
# and will not evaluate the remaining operators.

# The OR logical operator does the same with TRUE

good_credit = True
high_income = True
above_18 = True

if good_credit and high_income and above_18:
    print("Wow!")
else:
    print("Not so wow")

print("End")

# above python evaluated good_credit as True, so it continued to high_income which was True, so it finally checked
# above_18 and it was also True so the True function ran - print("wow!")
# If above_18 is changed to False python will evaluate good_credit as True and continue, high_income
# as True and continue then, lastly, above_18 as False: resulting in print("not so wow").
# Lastly, if good_credit is False then python will evaluate it as False, and not bother checking high_income or
# above_18. It will immediately jump to the else result.
