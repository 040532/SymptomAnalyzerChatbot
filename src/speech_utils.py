from gtts import gTTS
import os
from datetime import datetime

AUDIO_DIR = "static/audio"

def generate_audio_from_text(text, lang="en"):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"response_{timestamp}.mp3"
    filepath = os.path.join(AUDIO_DIR, filename)

    tts = gTTS(text=text, lang=lang)
    tts.save(filepath)
    return filename  # Just return the filename to be used in HTML
