def name_response(user_name):               #jlove
    print(f"Wow, {user_name} is such a beautiful name!")  # Include the name in the response


def main():
    user_name = input("What is your name? ")  # Collect user input
    name_response(user_name)  # Pass the input as an argument to name_response


if __name__ == "__main__":
    main()