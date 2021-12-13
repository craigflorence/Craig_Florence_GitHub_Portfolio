from questions_class import QuestionClass
# Below is a list of strings with 2 indexes, 0 and 1.

question_prompts = [
    "Apples are:\n(a) Red\n(b) Blue\n(c) Black\n\n",
    "Pears are:\n(a) Blue\n(b) Green\n(c)White"
]

# In the questions_class.py file the Questions class is defined.
# Use that new class to now turn the questions_prompts list of strings into a new list of Question objects

questions_array = [
    QuestionClass(question_prompts[0], "a"),
    QuestionClass(question_prompts[1], "b")
]

# In the new list questions_array there are 2 Questions_class objects.
# Make a function to ask the questions


def run_test(questions_to_ask):
    score = 0
    for q in questions_to_ask:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1
    print("You got " + str(score) + " / " + str((len(questions_array))))


run_test(questions_array)

# In the function the questions_array was passed in as the "questions_to_ask" iterable. Then for each of the contents of
# questions_to_ask, (being questions_array) the value q is compared.
