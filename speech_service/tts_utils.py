from django.conf import settings
import os
from uuid import uuid4
import pyttsx3

def text_to_speech(text, rate=None, format="wav"):
    engine = pyttsx3.init()
    if rate:
        engine.setProperty("rate", rate)   

    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

    filename = f"{uuid4()}.{format}"
    filepath = os.path.join(settings.MEDIA_ROOT, filename)

    engine.save_to_file(text, filepath)
    engine.runAndWait()

    return f"/media/{filename}"  # relative to MEDIA_URL
