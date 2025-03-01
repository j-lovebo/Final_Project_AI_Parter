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


def main():
    name = input("Enter your partner's name: ")
    age = int(input("Enter your partner's age: "))
    gender = input("Enter your partner's gender: ")
    appearance = input("Describe your partner's appearance: ")
    personality = input("Describe your partner's personality: ")

    partner = Partner(name, age, gender, appearance, personality)
    print(f"Meet your new partner: {partner}")

    pet_name = input("Enter your pet's name: ")
    pet_type = input("Enter the type of pet: ")
    pet = Pet(pet_name, pet_type)
    print(f"You have a new pet: {pet}")


if __name__ == "__main__":
    main()
