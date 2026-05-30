# Emotion Detection Web Application

![Flask](https://img.shields.io/badge/Flask-2.x-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![License](https://img.shields.io/badge/License-Apache%202.0-orange)

A Flask-based web application that detects emotions from user-provided text. The application analyzes input text and identifies five core emotions: **anger**, **disgust**, **fear**, **joy**, and **sadness**.

> 📝 **Note:** This project uses keyword-based emotion detection. For production environments, consider using machine learning models for more accurate results.

## Overview

This project implements an emotion detection system with a web interface and REST API. Users can submit text through a web form, and the system returns the detected emotions with confidence scores and identifies the dominant emotion.

## Features

- 🎯 **Emotion Detection**: Identifies 5 core emotions - anger, disgust, fear, joy, and sadness
- 🌐 **Web Interface**: User-friendly Flask-based web application
- 📊 **Confidence Scores**: Returns emotion scores for each detected emotion
- 🏆 **Dominant Emotion**: Identifies the primary emotion in the text
- ✅ **Unit Tests**: Comprehensive test coverage for all emotion types
- 🔧 **Error Handling**: Validates input and handles edge cases

## Project Structure

```
EmotionDetection/
├── EmotionDetection/              # Core emotion detection package
│   ├── __init__.py               # Package initialization
│   └── emotion_detection.py      # Main emotion detection algorithm
├── templates/                     # Flask HTML templates
│   └── index.html                # Web interface
├── static/                        # Static assets (CSS, JS, images)
├── server.py                      # Flask web server
├── test_emotion_detection.py      # Unit tests
├── requirements.txt               # Python dependencies
├── LICENSE                        # Apache License 2.0
└── README.md                      # This file
```

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/amit1330/EmotionDetection.git
cd EmotionDetection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

Start the Flask server:
```bash
python server.py
```

The application will be available at `http://localhost:5000`

### Using the API

Send a GET request to analyze emotions:
```bash
curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20really%20happy"
```

Expected response:
```
For the given statement, the system response is 'anger': 0.0 , 'disgust': 0.0 , 'fear': 0.0 , 'joy': 0.95 and 'sadness': 0.0 . The dominant emotion is joy.
```

## Supported Emotions

The system detects the following emotions:

| Emotion | Keywords |
|---------|----------|
| **Joy** | happy, joy, glad, excited |
| **Sadness** | sad, upset, cry |
| **Anger** | angry, mad, furious |
| **Fear** | fear, afraid, scared |
| **Disgust** | disgust, disgusted |

## Testing

Run the test suite:
```bash
python -m pytest test_emotion_detection.py
```

Or using unittest:
```bash
python -m unittest test_emotion_detection.py
```

Tests verify emotion detection for each of the five core emotions.

## API Endpoints

### GET /
Renders the web interface for emotion detection.

### GET /emotionDetector
Analyzes emotion from provided text.

**Parameters:**
- `textToAnalyze` (required): The text to analyze for emotions

**Returns:**
- Formatted string with individual emotion scores and dominant emotion
- "Invalid text! Please try again!" if input is empty

## Dependencies

- **Flask**: Web framework for building the web application
- **requests**: HTTP library for making requests
- **pytest**: Testing framework
- **pylint**: Code quality checker

See `requirements.txt` for the complete list of dependencies.

## License

This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.

## Author

Copyright 2020 IBM Developer Skills Network

## How It Works

The emotion detection system uses **keyword matching** to analyze text:

1. **Input Analysis**: The application receives text input from the user
2. **Keyword Matching**: Text is scanned for predefined emotion-related keywords
3. **Score Calculation**: Confidence scores are calculated for each emotion (0.0 - 1.0)
4. **Dominant Detection**: The emotion with the highest score is identified as dominant
5. **Response**: Results are returned with all scores and the dominant emotion

### Edge Cases Handled

- **Empty Input**: Returns "Invalid text! Please try again!"
- **No Keywords Matched**: A default emotion is assigned with a score of 0.5
- **Multiple Emotions**: The emotion with the highest score is marked as dominant

## Getting Started

### Quick Start (Windows)

```bash
# Create a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py
```

Then navigate to `http://localhost:5000` in your browser.

### Quick Start (macOS/Linux)

```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Port 5000 already in use** | Change port in `server.py` or kill the process using the port |
| **Module not found error** | Ensure virtual environment is activated and dependencies are installed |
| **No emotion detected** | Try using keywords from the supported emotions table |

## Future Enhancements

- [ ] Integration with NLP libraries (NLTK, TextBlob)
- [ ] Machine learning-based emotion detection
- [ ] Support for multiple languages
- [ ] Sentiment analysis alongside emotion detection
- [ ] Database storage for emotion history
- [ ] RESTful API with JSON responses
- [ ] Docker containerization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Notes

- The emotion detection is based on keyword matching in the input text
- Empty strings are treated as invalid input
- If no keywords are matched, a random emotion is assigned with a score of 0.5
- This is an educational project demonstrating Flask and emotion analysis concepts
