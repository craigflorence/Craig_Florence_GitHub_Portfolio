# When comparing strings, the word is sorted, then compared alphabetically. The later in the alphabet 
# it is, the higher the value.

"bag" > "cat"

# bag = abg, cat = act - bag, therefore comes before cat so SMALLER > BIGGER is False

print("bag" > "cat")

"differential" < "differentiate"
# so adeeffiilnrt < adeeeffiinrtt BIGGER < SMALLER is False

print("differential" < "differentiate")