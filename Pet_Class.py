class Pet:          #jlove
    def __init__(self, name, pet_type, color, personality):
        self.name = name
        self.pet_type = pet_type
        self.color = color
        self.personality = personality

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type}, color={self.color}, personality={self.personality})"


