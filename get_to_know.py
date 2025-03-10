def ask_worry():
    worry_response = input("Is anything worrying you? (yes/no) ").lower()

    if worry_response == "yes":
        print("I'm really sorry to hear that. It's okay to feel this way sometimes. Would you like to talk about it?")
        talk_response = input("(yes/no) ").lower()
        if talk_response == "yes":
            print("Sometimes sharing your feelings can help. I'm here to listen.")
        else:
            print("That's okay too. Remember, it's important to take care of yourself.")
    elif worry_response == "no":
        print("That's great to hear! It's always good to feel at ease.")
    else:
        print("I didn't quite understand that. Let's move on.")


    destress_response = input("What do you do to destress? ").lower()           #destress


    if destress_response:
        print(f"That's a good way to relax! Personally, I like to take long walks on the beach. It helps me clear my mind.")
    else:
        print("It's important to find something that helps you relax. Maybe try taking a walk or listening to music?")


def main():
    print("Im loving the conversations we are having:)")
    ask_worry()
    print("Thanks for sharing! Remember, it's okay to take things one step at a time. MUAHAHAH!")


if __name__ == "__main__":
    main()