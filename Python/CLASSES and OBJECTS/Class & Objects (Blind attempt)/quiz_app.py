from quiz_class import Question

question_prompts = [
    "Apples:\na) Red\nb) Blue",
    "Bananas:\na) Black\nb) Yellow"

]

question_array = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b")

]

def quiz(questions):
    score = 0
    for qs in question_array:
        answer = input(qs.prompt)
        if answer == qs.answer:
            score += 1
    print(f"You got {score}/{len(question_array)}")

quiz(question_array)