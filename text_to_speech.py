import pyttsx3


def convert_to_speech(filename):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    # engine.setProperty('rate', 150)  # Speed of speech
    # engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)

    # Extract text from the document
    with open(filename, "r", encoding='utf-8') as file:
        text = file.read()

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()
