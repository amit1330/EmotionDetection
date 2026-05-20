"""Unit tests for emotion detector."""

from EmotionDetection import emotion_detector


def test_emotion_detector():
    """Test dominant emotions."""

    sentences = {
        'I am glad this happened': 'joy',
        'I am really mad about this': 'anger',
        'I feel disgusted just hearing this': 'disgust',
        'I am so sad about this': 'sadness',
        'I am afraid this will happen': 'fear'
    }

    for text, emotion in sentences.items():
        response = emotion_detector(text)

        assert response['dominant_emotion'] == emotion