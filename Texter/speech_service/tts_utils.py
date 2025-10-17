import os, uuid, pyttsx3
from django.conf import settings

def text_to_speech(text: str, format='wav', rate=None):
    filename_prefix = 'tts_' + uuid.uuid4().hex[:8]
    tts_dir = os.path.join(settings.MEDIA_ROOT, 'tts')
    os.makedirs(tts_dir, exist_ok=True)
    ext = 'wav' if format not in ('mp3', 'wav') else format
    filename = f"{filename_prefix}.{ext}"
    out_path = os.path.join(tts_dir, filename)

    engine = pyttsx3.init()
    if rate: engine.setProperty('rate', rate)
    engine.save_to_file(text, out_path)
    engine.runAndWait()
    engine.stop()

    return {"audio_path": f"{settings.MEDIA_URL}tts/{filename}", "filename": filename}
       