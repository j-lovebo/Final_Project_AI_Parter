def analyze_day(userResponse):      #theo
    emotions = {
        "happy": ["good", "great", "awesome", "fantastic", "joyful", "amazing", "fun", "silly", "eventful", "wonderful", "Nice"],
        "sad": ["bad", "terrible", "horrible", "depressed", "upset", "down", "lonely", "sad", "not", "awful", "hard"],
        "angry": ["mad", "furious", "annoyed", "frustrated", "irritated", "difficult", ],
        "neutral": ["okay", "fine", "alright", "meh", "normal", "ok"]
    }
    #tracking the emotions by identifying possible keywords in the user's response and reacting in different
    #ways to each one

    while True:
        try:
            emotion_counts = {emotion: 0 for emotion in emotions}  # start counts
            words = userResponse.lower().split()  # Split response into words to check each word

            # count numbers of each emotion
            for word in words:
                for emotion, keywords in emotions.items():
                    if word in keywords:
                        emotion_counts[emotion] += 1

            max_count = max(emotion_counts.values())
            dominant_emotions = [emotion for emotion, count in emotion_counts.items() if count == max_count]

            if max_count == 0:  # runs code again if response wasn't in the code list
                raise ValueError(
                    "Oh, sorry! I didn't quite understand that. Can you try again?")

            if len(dominant_emotions) > 1:  # for when there are multiple emotions used by user
                response = "It seems like your day was "
                for i, emotion in enumerate(dominant_emotions):
                    if i == len(dominant_emotions) - 1 and len(dominant_emotions) > 1:
                        response += "and " + emotion + "."
                    else:
                        response += emotion + ", "
                response += " Hopefully it will get better!"
                print(response)
                break  # Exit loop and ask for clarification

            else:  #for when there is a clear dominant emotion from the user
                dominant_emotion = dominant_emotions[0]
                if dominant_emotion == "happy":  #response to happy keywords
                    print("I'm glad to hear that! You deserve a good day everyday!")
                elif dominant_emotion == "sad":  #response to sad keywords
                    print("I'm sorry to hear that, it's okay to feel down sometimes,"
                          "but just remember that everyone has tough days. Try to do "
                          "something that you know makes you happy!")
                elif dominant_emotion == "angry":  #response to angry keywords
                    print("That sounds frustrating, try to take some deep breathes to calm yourself down :)")
                elif dominant_emotion == "neutral":  #response to neutral keywords
                    print("Nothing wrong with a chill day:)")
                break  # Exit loop after responding

        except ValueError as e:
            print(e)
            userResponse = input("How was your day? ")  # Re-prompt if no emotions are detected


def main():
    response1 = input("Tell me about your day! ")
    analyze_day(response1)


if __name__ == "__main__":
    main()
