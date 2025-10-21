from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import re

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def extract_topics(text, n_topics=5):
    try:
        cleaned = clean_text(text)
        vectorizer = CountVectorizer(stop_words='english')
        X = vectorizer.fit_transform([cleaned])

        lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        lda.fit(X)

        feature_names = vectorizer.get_feature_names_out()
        topics_list = []

        for topic_idx, topic in enumerate(lda.components_):
            top_words = [feature_names[i] for i in topic.argsort()[:-6:-1]]
            topics_list.append(" ".join(top_words))

        return "; ".join(topics_list)  # return as a single string for TextField
    except Exception as e:
        print("Topic extraction error:", e)
        return "No topics found"
