

questions = ["How are you doing?", "What is your name?", "Can you tell me more?", "Is anything worrying you?"]

follow up questions based on response
follow up = 
{"positive": ["That's awesome! What made it so great?", "I love to hear that! Want to share more?"]
"negative": ["I'm here for you. Want to talk about it?", "That sounds tough. What happened?"], 
"neutral": ["Gotcha. Anything interesting going on?", "Fair enough. Anything on your mind?"]
}
def main():
    for question in questions:
        print(question)
        user_input = input()
        response = analyze_input(user_input)
        print(response)

  
