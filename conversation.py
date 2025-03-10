def analyze_day(userResponse):
    emotions = {
        "happy": ["good", "great", "awesome", "fantastic", "joyful", "amazing", "fun", "silly", "eventful"],
        "sad": ["bad", "terrible", "horrible", "depressed", "upset", "down", "lonely", "sad", "not"],
        "angry": ["mad", "furious", "annoyed", "frustrated", "irritated", "difficult", "hard"],
        "neutral": ["okay", "fine", "alright", "meh", "normal", "ok"]
    }

    while True:
        try:
            emotion_counts = {emotion: 0 for emotion in emotions}  # Initialize counts
            words = userResponse.lower().split()  # Split response into words

            # Count occurrences of each emotion
            for word in words:
                for emotion, keywords in emotions.items():
                    if word in keywords:
                        emotion_counts[emotion] += 1

            max_count = max(emotion_counts.values())
            dominant_emotions = [emotion for emotion, count in emotion_counts.items() if count == max_count]

            if max_count == 0:
                raise ValueError(
                    "Oh, sorry! I didn't quite understand that. Can you try again?")  # runs code again if response wasnt in domain

            if len(dominant_emotions) > 1:  # for ties
                response = "It seems like your day was "
                for i, emotion in enumerate(dominant_emotions):
                    if i == len(dominant_emotions) - 1 and len(dominant_emotions) > 1:
                        response += "and " + emotion + "."
                    else:
                        response += emotion + ", "
                response += " Hopefully it will get better!"
                print(response)
                break  # Exit loop and ask for clarification

            else:
                dominant_emotion = dominant_emotions[0]
                if dominant_emotion == "happy":
                    print("I'm glad to hear that! You deserve a good day everyday!")
                elif dominant_emotion == "sad":
                    print("I'm sorry to hear that, the day's not over to cheer up!")
                elif dominant_emotion == "angry":
                    print("That sounds frustrating, time to chillax.")
                elif dominant_emotion == "neutral":
                    print("Sounds like a chill day:)")
                break  # Exit loop after responding

        except ValueError as e:
            print(e)
            userResponse = input("How was your day? ")  # Re-prompt if no emotions are detected


def main():
    response1 = input("How was your day? ")
    analyze_day(response1)


if __name__ == "__main__":
    main()