def main():
    for question in questions:
        print(question)
        user_input = input()
        response = analyze_input(user_input)
        print(response)


