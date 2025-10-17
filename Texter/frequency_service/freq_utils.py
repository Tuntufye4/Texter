import re
from collections import Counter
import spacy
nlp = spacy.load("en_core_web_sm")

def word_frequency(text: str, top_n=50, remove_stopwords=True):
    doc = nlp(text.lower())
    words = [token.text for token in doc if token.is_alpha]
    if remove_stopwords:
        words = [w for w in words if not nlp.vocab[w].is_stop]
    return dict(Counter(words).most_common(top_n))
