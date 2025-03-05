class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type})"
