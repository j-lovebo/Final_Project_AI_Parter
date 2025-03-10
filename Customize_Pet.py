from Pet_Class import Pet  # Importing Pet class from pet_data.py

def customize_pet():
    print("I'm thinking about getting a pet. Please help me customize them!")

    pet_name = input("What should we name the pet? ")
    pet_type = input("What kind of pet should we get? ")
    pet_color = input("What color should the pet be? ")
    pet_personality = input("What personality trait should the pet have? ")

    # Create a Pet object with user input
    new_pet = Pet(pet_name, pet_type, pet_color, pet_personality)

    # Print the pet's details
    print(f"Awesome! We now have a {new_pet.color} {new_pet.pet_type} named {new_pet.name} who is very {new_pet.personality}!")

def main():
    customize_pet()

if __name__ == "__main__":
    main()
