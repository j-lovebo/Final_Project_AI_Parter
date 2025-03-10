import random

# List of questions to ask the user
#Theo
questions = [
    "Are you doing anything fun today?",
    "What is your favorite hobby?",
    "Can you tell me something interesting about yourself?",
    "What is the best thing that happened this week?",
    "Is there anything you're excited about right now?",
    "What’s something you’ve been thinking a lot about lately?",
    "What makes you happy?",
    "What’s something you want to achieve soon?",
    "Do you have a favorite subject in school?"
]

responses = [
    "Very interesting.",
    "That's good to hear.",
    "Nice, that sounds really cool!",
    "That's really insightful",
    "I appreciate you telling me that.",
    "Cool thoughts",
    "Wow, how cool!"
]



def ask_random_question():

    random.shuffle(questions) #shuffles the questions so that they are asked at random

    for question in questions:
        user_input = input(question + " ") #gets the users response after asking question
        print(random.choice(responses))

    print("Thanks for talking with me today, see you later!")



def main():
    ask_random_question()

if __name__ == "__main__":
    main()



