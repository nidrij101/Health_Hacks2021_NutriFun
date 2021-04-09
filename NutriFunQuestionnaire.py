# Importing Question function from Question.py
from Question import Question

question_prompts = [
    "1. How many servings of GRAINS (Bread, Cereal, Rice, & Pasta) do you eat per day?\n\n",
    "2. How many servings of VEGETABLES do you eat per day?\n\n",
    "3. How many servings of FRUIT do you eat per day?\n\n",
    "4. How many servings of PROTEIN (Meat, Poultry, Fish, Dry Beans, Eggs, & Nuts) do you eat per day?\n\n",
    "5. How many servings of DAIRY (Milk, Yogurt, & Cheese) do you eat per day?\n\n",
    "6. How many servings of FAT & SWEET (Fats, Oils, & Sweets) do you eat per day?\n\n",
]

# Using Question function to create questions, answers, and some additional information
questions = [
    Question(question_prompts[0], range(6, 12, 1), "6 to 11", "grains"),
    Question(question_prompts[1], range(3, 6, 1), "3 to 5", "vegetables"),
    Question(question_prompts[2], range(2, 5, 1), "2 to 4", "fruits"),
    Question(question_prompts[3], range(2, 4, 1), "2 to 3", "proteins"),
    Question(question_prompts[4], range(2, 4, 1), "2 to 3", "dairy"),
    Question(question_prompts[5], range(1, 3, 1), "1 to 2", "fats & sweets"),
]


# This function goes from one question to the next using the questions array
def question1to6(questions):
    for question in questions:
        answer = int(raw_input(question.prompt))
        if answer in question.answer:
            print("This is the right amount you should be eating per day for " + question.item)
        else:
            print("You need to eat " + question.item + ", " + question.serving_size + " servings per day")


# Using try, except, and else because if there is an error we can give our own custom error so it is easier for
# people that don't know python
try:
    question1to6(questions)

    # Trying to figure out how heavy and how much you water you drink just to see if you are healthy
    weight_question = int(raw_input("7. How much do you weigh in pounds?\n\n"))
    water_question = int(raw_input("8. How many ounces of WATER do you drink?\n\n", ))

    if water_question < weight_question * 1 / 2:
        print("You need to drink " + str(weight_question * 1 / 2) + " ounces as per your weight")
    elif water_question > weight_question + 3:
        print("Drink a little bit less water because you are drinking " + str(
            water_question - (weight_question + 3)) + " more ounces than needed")
    else:
        print("Good Job! This is the right amount of water you should drink per day!")

except BaseException as e:
    print(str(e) + ", so please enter an integer.\nExample: 1")

else:
    print("\n******************************************")
    print("\nThank you for using NutriFun")
    print("\n******************************************")
