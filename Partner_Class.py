
class Partner:
    def __init__(self, name, age, gender, appearance, personality):
        self.name = name
        self.age = age
        self.gender = gender
        self.appearance = appearance
        self.personality = personality

    def __repr__(self):
        return f"Partner(name={self.name}, age={self.age}, gender={self.gender}, appearance={self.appearance}, personality={self.personality})"

name = input("Enter name: ")
gender = input("Enter gender: ")
age = int(input("Enter age: "))
appearance = input("Enter appearance: ")
personality = input("Enter personality: ")

partner = Partner(name, age, gender, appearance, personality)

class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type})"

    def show_pet(self):
        print(f"You have a {self.pet_type} named {self.name}!")

pet_name = input("Enter pet's name: ")
pet_type = input("Enter pet's type: ")

pet = Pet(pet_name, pet_type)