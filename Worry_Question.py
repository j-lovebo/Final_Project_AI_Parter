#theo and jlove

def ask_worry():
    worry_response = input("Is anything specific worrying you lately? (yes/no) ").lower()

    if worry_response == "yes":  #talking to user if they have something worrying them
        print("I'm really sorry to hear that. It's okay to feel this way sometimes. Would you like to talk about it?")
        talk_response = input("(yes/no) ").lower()

        if talk_response == "yes":  #talking to user if they want to talk
            print("Sometimes sharing your feelings can help.")

            user_feelings = input("Tell me about it :) ")  #lets user talk about their feelings
            print(f"Thanks for sharing. You've made a great first step in tackling this struggle. Just remember it will get better!")
        elif talk_response == "no":  #if user does not want to talk
            print("That's okay too. Remember, it's important to take care of yourself.")
        else:   #if user does not respond yes or no
            print("I didn't quite understand that. Let's move on.")

    elif worry_response == "no":  #if user does not have any worries
        print("That's great to hear! It's always good to feel at ease.")
    else:  #if user does not respond with yes or no
        print("I didn't quite understand that. Let's move on.")

    #moves on and ask about user's stress
    destress_response = input("What do you do to destress? ").lower()           #destress


    if destress_response:  #responding to what the user does to destress
        print(f"That's a good way to relax! Personally, I like to take long walks on the beach. It helps me clear my mind. It was awesome chatting with you I hope we can talk soon again.")
    else:  #if the user does not respond
        print("It's important to find something that helps you relax. Maybe try taking a walk or listening to music? It was awesome chatting with you I hope we can talk soon again.")


def main():
    print("I'm loving the conversations we are having:)")
    ask_worry()
    print("Thanks for sharing! Remember, it's okay to take things one step at a time. MUAHAHAH!")


if __name__ == "__main__":
    main()
