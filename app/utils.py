import os
from gtts import gTTS


def create_audio(text, audio_file):
    language = 'en'
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save(audio_file)


# def download_audio(audio_file):
#     uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
#     print(uploads)
