import Partner_Class


def ask_question(huh: data.Partner_Class):

    question = "How was your day?"
    print(f"{self.name}: {question}")
    response = input("Your response: ")
    self.analyze_response(response)


def analyze_response(self, response):
    """Analyzes the user's response and determines the most common emotion."""
    emotions = {
        "happy": ["good", "great", "amazing", "fantastic", "awesome"],
        "sad": ["bad", "terrible", "awful", "depressed", "upset"],
        "angry": ["mad", "angry", "furious", "annoyed", "irritated"],
        "neutral": ["okay", "fine", "alright", "meh", "normal"]