from textblob import TextBlob


def analyze_sentiment(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    blob = TextBlob(text)
    sentiment_scores = {
        "Polarity": blob.sentiment.polarity,
        "Subjectivity": blob.sentiment.subjectivity
    }

    return sentiment_scores

