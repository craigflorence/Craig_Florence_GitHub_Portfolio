user_name = input("What is your name? ")
print("Your name is " + user_name + "!")

value_1 = input("What is your first number? ")
value_2 = input("What is your second number? ")
value_sum = value_1 + value_2
print("They add up to " + str(value_sum))

# What? Its concatenating the values instead of doing maths.

value_sum = int(value_1) + int(value_2)
print("They add up to " + str(value_sum))

# So the result saved to the Variables from input() is stored as a string. Use the Int() function to convert back
# to integers. BUT if you need to use decimal places use float().

# ----------------------------------------- MAD LIBS ----------------------------------------

your_name = input("What is your name?: ")
verb_1 = input("Verb ending in S like jumps: ")
verb_2 = input("and another: ")
verb_3 = input("another!: ")
verb_4 = input("... one more verb: ")
body_1 = input("A part of your body: ")
body_2 = input("Another part of your body: ")
body_3 = input("ANOTHER!: ")
body_4 = input("MORE BODY PARTS: ")
body_5 = input("YES! GIVE ME MORE!: ")
body_6 = input("Ugh... are there any parts left?: ")
body_7 = input("Oh that was a good one. Some more: ")
body_8 = input("Last one!: ")
body_9 = input("I lied. This is the last one: ")
body_10 = input("I lied again. Can you even think of more body parts? Have you tried nipples yet?: ")
body_11 = input("Heads, shoulders knees and toes...: ")
body_12 = input("Ok this is the last one: ")
adj_1 = input("Adjective 1/5: ")
adj_2 = input("Adjective 2/5: ")
adj_3 = input("Adjective 3/5: ")
adj_4 = input("Adjective 4/5: ")
adj_5 = input("Adjective 5/5: ")
adj_6 = input("I lied again. Adjective 6/6: ")
noun = input("Give me a noun: ")
noun_2 = input("One more noun: ")
noun_3 = input("Last noun: ")
adverb = input("One adverb, like loudly, quickly: ")
ing_verb = input("And. Finally. An -ing verb: ")

mad_lib = "He " + verb_1 + " his " + body_1 + " so his " + body_2 + " pushes against me... \nYes! right there! " \
    "He " + verb_2 + " his " + body_3 + " along my \n" + body_4 + ", eases back, then " + verb_3 + " into me again - " \
    "so " + adj_1 + ", so \n" + adj_2 + "so " + adj_3 + "- his " + body_5 + " pressing down on me, " \
    "his \n" + body_6 + " " \
    "on either side of my " + body_7 + ". 'Oh, \n" + your_name + "' he " + verb_4 + " as he lets go, my name " \
    "a " + noun + " on his \n" \
    + body_8 + " as he finds his " + noun_2 + ". His \n" + body_9 + " rests on my " + body_10 + ", his \n" + body_11 \
    + " wrapped around me... I just want to enjoy the " + adverb + " " + adj_4 + " afterglow of making \n" + noun_3 \
    + " with him, because that is what we have done: \n" \
    + adj_5 + ", " + adj_6 + " " + ing_verb

print(mad_lib)
