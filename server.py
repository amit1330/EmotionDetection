"""
Emotion Detection Flask Server
"""

from flask import Flask
from flask import render_template
from flask import request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """
    Render the index page
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze emotions from user input
    """

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        "For the given statement, the system response is "
        "'anger': {} , "
        "'disgust': {} , "
        "'fear': {} , "
        "'joy': {} and "
        "'sadness': {}. "
        "The dominant emotion is {}."
    ).format(
        response['anger'],
        response['disgust'],
        response['fear'],
        response['joy'],
        response['sadness'],
        response['dominant_emotion']
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)