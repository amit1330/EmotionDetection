import random


def emotion_detector(text_to_analyze):
    """
    Detect emotions from text
    """

    if text_to_analyze.strip() == "":
        return None

    text = text_to_analyze.lower()

    emotions = {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0
    }

    if any(word in text for word in ['happy', 'joy', 'glad', 'excited']):
        emotions['joy'] = 0.95

    elif any(word in text for word in ['sad', 'upset', 'cry']):
        emotions['sadness'] = 0.95

    elif any(word in text for word in ['angry', 'mad', 'furious']):
        emotions['anger'] = 0.95

    elif any(word in text for word in ['fear', 'afraid', 'scared']):
        emotions['fear'] = 0.95

    elif any(word in text for word in ['disgust', 'disgusted']):
        emotions['disgust'] = 0.95

    else:
        emotions[random.choice(list(emotions.keys()))] = 0.5

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }