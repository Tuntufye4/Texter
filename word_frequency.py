from collections import Counter


def calculate_word_frequency(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Split the text into words
    words = text.split()

    # Calculate word frequency using Counter
    word_freq = Counter(words)

    return word_freq
