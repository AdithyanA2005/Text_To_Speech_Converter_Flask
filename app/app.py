from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from app.utils import create_audio
import datetime
import os

app = Flask(__name__)
app.config['AUDIO_FOLDER'] = os.path.join(app.root_path, "static/audios")


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
    def delete():
        directory = app.config['AUDIO_FOLDER']
        files_in_directory = os.listdir(directory)
        print(f"filesindirectory {files_in_directory}")
        filtered_files = [file for file in files_in_directory if file.endswith(".mp3")]
        print(f"Filtered LIst {filtered_files}")
        for file in filtered_files:
            print(f"- {file}")
	        path_to_file = os.path.join(directory, file)
            print(f"     path {path_to_file}")
            os.remove(path_to_file)

    text = request.args.get('text_to_convert')
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = "audio_" + date + ".mp3"
    delete()
    create_audio(text, app.config['AUDIO_FOLDER'] + filename)
    return redirect(url_for("home", text=text, file=filename))
