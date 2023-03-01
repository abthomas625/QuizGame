import random

print("Welcome to my computer quiz!")

playing = input("Would you like to play? ").lower()

if playing != "yes":
    quit()

print("Great! Let's get started!")
qa_dict = {
    "Who is the current president of the United States? ": "Joe Biden",
    "What is the largest continent on Earth? ": "Asia",
    "What is the capital of the United States? ": "Washington, D.C.",
    "Who wrote the famous novel 'To Kill a Mockingbird'? ": "Harper Lee",
    "Who painted the famous artwork 'The Mona Lisa'? ": "Leonardo da Vinci",
    "What is the smallest planet in our solar system? ": "Mercury",
    "Who is the famous scientist that developed the theory of relativity? ": "Albert Einstein",
    "What is the largest mammal on Earth? ": "Blue whale",
    "What is the name of the country where the Great Pyramid of Giza is located? ": "Egypt",
    "What is the largest ocean on Earth? ": "Pacific Ocean"
}
go_on = True
while go_on == True:
    correct = 0
    keys = list(qa_dict.keys())
    random.shuffle(keys)
    for key in keys:
        answer = input(key)
        if answer.lower() == qa_dict[key].lower():
            print("That's correct!")
            correct += 1
        else:
            print("That's incorrect.")
    print(f"You got {str(correct)} out of {len(qa_dict)} questions correct")
    response = input("Would you like to go again? ")
    if response == "yes":
        go_on = True
        continue
    elif response == "no":
        go_on = False
        quit()