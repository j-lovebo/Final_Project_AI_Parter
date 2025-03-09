def analyze_day(userResponse):
    emotions = {
        "happy": ["good", "great", "awesome", "fantastic", "joyful", "amazing", "fun", "silly", "eventful"],
        "sad": ["bad", "terrible", "horrible", "depressed", "upset", "down", "lonely", "sad", "not"],
        "angry": ["mad", "furious", "annoyed", "frustrated", "irritated", "difficult", "hard"],
        "neutral": ["okay", "fine", "alright", "meh", "normal", "ok"]
    }

    while True:  # try exception, keeps the code running until it's in the domain
        try:
            emotion_counts = {emotion: 0 for emotion in emotions}  # Initialize
            words = userResponse.lower().split()

            for word in words:
                for emotion, keywords in emotions.items():
                    if word in keywords:
                        emotion_counts[emotion] += 1

            dominant_emotion = max(emotion_counts, key=emotion_counts.get)

            if emotion_counts[dominant_emotion] == 0:
                raise ValueError("Oh, sorry! I didn't quite understand that. Can you try again?")

            if dominant_emotion == "happy":     # Respond based on the dominant emotion
                print("I'm glad to hear that! You deserve a good day everyday!")
            elif dominant_emotion == "sad":
                print("I'm sorry to hear that, the days not over to cheer up!")
            elif dominant_emotion == "angry":
                print("That sounds frustrating, time to chillax.")
            elif dominant_emotion == "neutral":
                print("Sounds like a chill day:)")

            break  #finishes loop when properly responded

        except ValueError as e:
            print(e)  # Print the error message
            userResponse = input("How was your day? ")  # runs again if error happens


def main():
    response1 = input("How was your day? ")
    analyze_day(response1)


if __name__ == "__main__":
    main()