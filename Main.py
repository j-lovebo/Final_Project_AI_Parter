from Analyze_Day import analyze_day
from Worry_Question import ask_worry
from Customize_Pet import customize_pet
from Customize_Partner import customize_partner


def main():

    customize_partner()  #Start by making the user's partner

    customize_pet()  #Then do the same but with the partner's pet

    response_day = input("How was your day? ")  #Run conversation code, talking about the user's day
    analyze_day(response_day)

    ask_worry() #run get to know code, asking about what is worrying user


if __name__ == "__main__":  #make sure script runs
    main()


