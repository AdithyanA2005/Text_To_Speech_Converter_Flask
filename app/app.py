from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from app.utils import create_audio
import datetime
import os

app = Flask(__name__)
app.config['AUDIO_FOLDER'] = os.path.join(app.root_path, "static/")


@app.route('/')
def home():
    def get_text():
        text = request.args.get('text')
        return "" if text == None else text


    def get_audio():
        file = request.args.get('file')
        return "" if file == None else file


    return render_template('index.html', get_text=get_text(), get_audio=get_audio())


@app.route("/convert", methods=['POST', 'GET'])
def convert():
    text = request.args.get('text_to_convert')
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = "audio_" + date + ".mp3"
    create_audio(text, app.config['AUDIO_FOLDER'] + filename)
    return redirect(url_for("home", text=text, file=filename))
