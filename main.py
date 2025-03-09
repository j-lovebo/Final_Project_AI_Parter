from Partner_Class import Partner
from Pet_Class import Pet
from Questions import questions, follow_up

def get_user_input(questions): 
    responses = []
    for question in questions: 
        responses.append(input(question))
    return responses


def main():
    #collecting input for making partner
    name = input("Enter your partner's name: ")
    age = int(input("Enter your partner's age: "))
    gender = input("Enter your partner's gender: ")
    appearance = input("Describe your partner's appearance: ")
    personality = input("Describe your partner's personality: ")

    #creates the user's partner
    partner = Partner(name, age, gender, appearance, personality)
    print(f"Meet your new partner: {partner}")

    #collecting input for making pet
    pet_name = input("Enter your pet's name: ")
    pet_type = input("Enter the type of pet: ")

    #create user's pet
    pet = Pet(pet_name, pet_type)
    print(f"You have a new pet: {pet}")



if __name__ == "__main__":
    main()



