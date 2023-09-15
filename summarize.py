from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def summarize_document(filename):
    # Extract text from the document
    with open(filename, "r", encoding='utf-8') as file:
        text = file.read()

    # Initialize the parser and tokenizer
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Initialize the summarizer
    summarizer = LsaSummarizer()

    # Summarize the document
    summary = summarizer(parser.document, 1)  # Set the number of sentences in the summary

    return " ".join([str(sentence) for sentence in summary])
