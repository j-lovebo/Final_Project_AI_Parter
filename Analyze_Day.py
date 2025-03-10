def analyze_day(userResponse):
    emotions = {
        "happy": ["good", "great", "awesome", "fantastic", "joyful", "amazing", "fun", "silly", "eventful"],
        "sad": ["bad", "terrible", "horrible", "depressed", "upset", "down", "lonely", "sad", "not"],
        "angry": ["mad", "furious", "annoyed", "frustrated", "irritated", "difficult", "hard"],
        "neutral": ["okay", "fine", "alright", "meh", "normal"]
    }

    while True:  # Keep retrying if there's an error
        try:
            emotion_counts = {emotion: 0 for emotion in emotions}  # Initialize counters
            words = userResponse.lower().split()

            for word in words:
                for emotion, keywords in emotions.items():
                    if word in keywords:
                        emotion_counts[emotion] += 1

            dominant_emotion = max(emotion_counts, key=emotion_counts.get)

            if emotion_counts[dominant_emotion] == 0:
                raise ValueError("Oh, sorry! I didn't quite understand that. Can you try again?")

            # Respond based on the dominant emotion
            if dominant_emotion == "happy":
                print("I'm glad to hear that! What made your day so great?")
            elif dominant_emotion == "sad":
                print("I'm sorry to hear that. Do you want to talk about it?")
            elif dominant_emotion == "angry":
                print("That sounds frustrating. What happened?")
            elif dominant_emotion == "neutral":
                print("Got it. Anything interesting happen today?")

            break  # Exit loop if a valid response is given

        except ValueError as e:
            print(e)  # Print the error message
            userResponse = input("How was your day? ")  # Ask for input again


def main():
    response1 = input("How was your day? ")
    analyze_day(response1)


if __name__ == "__main__":
    main()
