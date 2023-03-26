quiz = {
    "question1" : {
        "question":"what is the capital of France?",
        "answer": "Paris"
    },
    "question2" : {
        "question": "what is the capital of Nigeria?",
        "answer": "Abuja"
    },
    "question3" : {
        "question" : "what is the capital of USA?",
        "answer": "Washington DC"
    },
    "question4" : {
        "question": "what is the capital of Ghana?",
        "answer": "Accra"
    }
 }

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("correct")
        score = score + 1
        print("Your score is: " + str(score))
        print("")

    else:
        print("Incorrect!")
        print("The answer is: " + value["answer"])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " " + "out of 4 questions correct")
print("Your percentage is " + str(int(score/4 * 100)) + "%")