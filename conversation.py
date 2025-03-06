response = str(input("How was your day?"))

def analyze_response(userResponse):
    emotions = {
        "happy": ["good", "great", "awesome", "fantastic", "joyful", "amazing", "fun", "silly", "eventful"],
        "sad": ["bad", "terrible", "horrible", "depressed", "upset", "down", "lonely", "sad", "not"],
        "angry": ["mad", "furious", "annoyed", "frustrated", "irritated", "difficult", "hard"],
        "neutral": ["okay", "fine", "alright", "meh", "normal"]
    }

    emotion_counts = {"happy": 0, "sad": 0, "angry": 0, "neutral": 0}       #initializing

    words = response.lower().split()

    for word in words:                                                     #counter
        for emotion, keywords in emotions.items():
            if word in keywords:
                emotion_counts[emotion] += 1

    try:
        dominant_emotion = max(emotion_counts, key=emotion_counts.get)         #finds most common expression

        if emotion_counts[dominant_emotion] == 0:
            raise ValueError("I bet tomorrow will be more eventful!")

        if dominant_emotion == "happy":
            print ("I'm glad to hear that! What made your day so great?")
        elif dominant_emotion == "sad":
            print ("I'm sorry to hear that. Do you want to talk about it?")
        elif dominant_emotion == "angry":
            print ("That sounds frustrating. What happened?")
        elif dominant_emotion == "neutral":
            print ("Got it. Anything interesting happen today?")

    except ValueError:                                                  #incase words used are not in the dict
        print ("Oh, sorry! I didn't quite understand that.")


def main():
    analyze_response(response)

if __name__ == "__main__":
    main()