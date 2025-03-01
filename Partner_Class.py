
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



if __name__ == "__main__":
    main()
