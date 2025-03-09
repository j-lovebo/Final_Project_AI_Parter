class Partner:
    def __init__(self, name, age, gender, appearance, personality):
        self.name = name
        self.age = age
        self.gender = gender
        self.appearance = appearance
        self.personality = personality

    def __repr__(self):
        return f"Partner(name={self.name}, age={self.age}, gender={self.gender}, appearance={self.appearance}, personality={self.personality})"


