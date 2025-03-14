def analyze_day(userResponse):
    while True:
        try:
            # Define possible emotions and associated keywords
            emotions = {
                "happy": ["good", "great", "awesome", "fantastic", "joyful", "amazing", "fun", "silly", "eventful", "wonderful", "nice"],
                "sad": ["bad", "terrible", "horrible", "depressed", "upset", "down", "lonely", "sad", "not", "awful", "hard"],
                "angry": ["mad", "furious", "annoyed", "frustrated", "irritated", "difficult"],
                "neutral": ["okay", "fine", "alright", "meh", "normal", "ok"]
            }

            emotion_counts = {emotion: 0 for emotion in emotions}
            words = userResponse.lower().split()

            # Count occurrences of each emotion
            for word in words:
                for emotion, keywords in emotions.items():
                    if word in keywords:
                        emotion_counts[emotion] += 1

            max_count = max(emotion_counts.values())
            dominant_emotions = [emotion for emotion, count in emotion_counts.items() if count == max_count]

            if max_count == 0:  # No emotions detected
                raise ValueError("Oh, sorry! I didn't quite understand that. Can you try again?")

            if len(dominant_emotions) > 1:  # Multiple emotions detected
                response = "It seems like your day was "
                if len(dominant_emotions) == 2:
                    response += f"{dominant_emotions[0]} and {dominant_emotions[1]}."
                else:
                    for i in range(len(dominant_emotions)):
                        if i == len(dominant_emotions) - 1:
                            response += f"and {dominant_emotions[i]}."
                        else:
                            response += f"{dominant_emotions[i]}, "
                response += " Hopefully it will get better!"
                return response

            # Single dominant emotion detected
            responses = {
                "happy": "I'm glad to hear that! You deserve a good day every day!",
                "sad": "I'm sorry to hear that. It's okay to feel down sometimes, but remember that everyone has tough days. Try to do something that makes you happy!",
                "angry": "That sounds frustrating. Try taking some deep breaths to calm yourself down. :)",
                "neutral": "Nothing wrong with a chill day! :)"
            }
            return responses[dominant_emotions[0]]

        except ValueError as e:
            print(e)
            userResponse = input("How was your day? ")  # Re-prompt user for a new response


def main():
    response = analyze_day(input("How was your day? "))
    print(response)


if __name__ == "__main__":
    main()
