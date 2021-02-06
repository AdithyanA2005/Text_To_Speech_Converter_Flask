from gtts import gTTS
import os


class Speech:
    def __init__(self, audio_file, text_file):
        self.txt_file = text_file
        self.audio_file = audio_file
        self.text = self.get_text()
        self.create_audio(self.text)
        self.play_sound()

    def play_sound(self):
        cmd = f"xdg-open {self.audio_file}"
        os.system(cmd)

    def get_text(self):
        text_file = open(self.txt_file, "r")
        text = text_file.read()
        print(text)
        return text

    def create_audio(self, text):
        language = 'en'
        audio = gTTS(text=text, lang=language, slow=False)
        audio.save(self.audio_file)
