import spacy


def recognize_entities(filename):
    nlp = spacy.load("en_core_web_sm")
    
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

