from Partner_Class import Partner  # Import the Partner class       #theo

def customize_partner():
    print("Let's start by customizing your partner!")

    # Collect user input for the partner's attributes
    name = input("What is your partner's name? ")
    age = int(input("How old is your partner? "))
    gender = input("What gender is your partner? ")
    appearance = input("Describe your partner's appearance: ")
    personality = input("What is your partner's personality like? ")

    # Create a Partner object using the collected input
    partner = Partner(name, age, gender, appearance, personality)

    # Print the partner's details
    print(f"Hello! I am your partner named {partner.name}, who is {partner.age} years old, "
          f"looks {partner.appearance}, and has a {partner.personality} personality!")

def main():
    customize_partner()

if __name__ == "__main__":
    main()
