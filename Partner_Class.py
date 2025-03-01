
class Partner:
    def __init__(self, name, age, gender, appearance, personality):
        self.name = name
        self.age = age
        self.gender = gender
        self.appearance = appearance
        self.personality = personality

    def __repr__(self):
        return f"Partner(name={self.name}, age={self.age}, gender={self.gender}, appearance={self.appearance}, personality={self.personality})"


class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type})"

    def show_pet(self):
        print(f"You have a {self.pet_type} named {self.name}!")

#positive_responses = [“good”, “happy”, “awesome”, “great”, “excited”]
#negative_responses = ["sad", "angry", "bad", "down", “terrible]

questions = ["How are you doing?", "What is your name?", "Can you tell me more?"]
             
def main():
    for question in questions:
        print(question)
        user_input = input()
        response = analyze_input(user_input)
        print(response)


