
def analyze_day(userResponse):  # jlove
    emotions = {
        "happy": ["good", "great", "awesome", "fantastic", "joyful", "amazing", "fun", "silly", "eventful", "wonderful", "nice"],
        "sad": ["bad", "terrible", "horrible", "depressed", "upset", "down", "lonely", "sad", "not", "awful", "hard"],
        "angry": ["mad", "furious", "annoyed", "frustrated", "irritated", "difficult"],
        "neutral": ["okay", "fine", "alright", "meh", "normal", "ok"]
    }

    emotion_counts = {emotion: 0 for emotion in emotions}  # start counts
    words = userResponse.lower().split()  # Split response into words to check each word

    # count numbers of each emotion
    for word in words:
        for emotion, keywords in emotions.items():
            if word in keywords:
                emotion_counts[emotion] += 1

    max_count = max(emotion_counts.values())
    dominant_emotions = [emotion for emotion, count in emotion_counts.items() if count == max_count]

    if max_count == 0:  # no emotions detected
        raise ValueError("Oh, sorry! I didn't quite understand that. Can you try again?")

    if len(dominant_emotions) > 1:  # for when there are multiple emotions used by user
        response = "It seems like your day was "
        for i, emotion in enumerate(dominant_emotions):
            if i == len(dominant_emotions) - 1 and len(dominant_emotions) > 1:
                response += "and " + emotion + "."
            else:
                response += emotion + ", "
        response += " Hopefully it will get better!"
        return response

    else:  # for when there is a clear dominant emotion from the user
        dominant_emotion = dominant_emotions[0]
        if dominant_emotion == "happy":  # response to happy keywords
            return "I'm glad to hear that! You deserve a good day everyday!"
        elif dominant_emotion == "sad":  # response to sad keywords
            return "I'm sorry to hear that, it's okay to feel down sometimes, but just remember that everyone has tough days. Try to do something that you know makes you happy!"
        elif dominant_emotion == "angry":  # response to angry keywords
            return "That sounds frustrating, try to take some deep breathes to calm yourself down :)"
        elif dominant_emotion == "neutral":  # response to neutral keywords
            return "Nothing wrong with a chill day:)"