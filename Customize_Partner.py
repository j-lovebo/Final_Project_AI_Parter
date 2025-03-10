      #theo

from Partner_Class import Partner  # Import the Partner class

def customize_partner(name=None, age=None, gender=None, appearance=None, personality=None):
    print("Let's start by customizing your partner!")

    # If the values are not passed as arguments, ask for user input
    if name is None:
        name = input("What is your partner's name? ")
    if age is None:
        age = int(input("How old is your partner? "))
    if gender is None:
        gender = input("What gender is your partner? ")
    if appearance is None:
        appearance = input("Describe your partner's appearance: ")
    if personality is None:
        personality = input("What is your partner's personality like? ")

    # Create a Partner object using the collected input
    partner = Partner(name, age, gender, appearance, personality)

    # Generate the partner's details string and return it
    result = f"Hello! I am your partner named {partner.name}, who is {partner.age} years old, " \
             f"looks {partner.appearance}, and has a {partner.personality} personality!"
    return result
