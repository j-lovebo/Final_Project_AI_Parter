from Analyze_Day import analyze_day
from Worry_Question import ask_worry
from Customize_Pet import customize_pet
from Customize_Partner import customize_partner
from name_reponse import name_response

#theo
def main():

    customize_partner()  #Start by making the user's partner

    user_name = input("What is your name? ")  # Collect the user's name
    name_response(user_name)

    customize_pet()  #Then do the same but with the partner's pet

    response_day = input("How was your day? ")  #Run conversation code, talking about the user's day
    analyze_day(response_day)

    ask_worry() #run get to know code, asking about what is worrying user


if __name__ == "__main__":  #make sure script runs
    main()


