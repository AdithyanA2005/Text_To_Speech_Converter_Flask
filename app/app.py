from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from app.utils import create_audio
import datetime
import os

app = Flask(__name__)
app.config['AUDIO_FOLDER'] = os.path.join(app.root_path, "static/audios/")
app.config['STATIC_FOLDER'] = os.path.join(app.root_path, "static/")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/converter')
def converter():
    def get_text():
        text = request.args.get('text')
        return "" if text is None else text

    def get_audio():
        file = request.args.get('file')
        return "" if file is None else file

    return render_template('app.html', get_text=get_text(), get_audio=get_audio())


@app.route("/convert", methods=['POST', 'GET'])
def convert():
    text = request.args.get('text_to_convert')
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = "audio_" + date + ".mp3"

    directory = app.config['AUDIO_FOLDER']
    files = os.listdir(directory)
    if len(files) > 5:
        for file in files:
            path_to_file = os.path.join(directory, file)
            if path_to_file.endswith('.mp3'):
                os.remove(path_to_file)

    create_audio(text, app.config['AUDIO_FOLDER'] + filename)
    return redirect(url_for("converter", text=text, file=filename))


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def notfound(e):
    return render_template('error.html')

