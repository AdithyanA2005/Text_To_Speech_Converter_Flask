from app.speech import Speech

if __name__ == '__main__':
    audio = "utils/audio.mp3"
    text = "utils/text.txt"
    app = Speech(audio, text)
