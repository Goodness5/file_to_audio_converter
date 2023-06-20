import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from gtts import gTTS
from langdetect import detect
from gtts.lang import tts_langs
import uuid
# from gtts.lang import get_available_voices



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['STATIC_FOLDER'] = 'static'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'docx', 'pdf'}
app.config['AVAILABLE_FORMATS'] = {'mp3', 'wav'}
# app.config['AVAILABLE_LANGUAGES'] = {'en', 'fr', 'es'}  # Add more languages as needed


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_available_voices(language):
    available_voices = []
    for lang_code, lang_name in tts_langs().items():
        if lang_code.startswith(language):
            available_voices.append(lang_name)
    return available_voices

def text_to_speech(text, language, voice, audio_format):
    # Generate a unique filename for the audio file
    filename = f"{uuid.uuid4().hex}.{audio_format}"

    # Define the output file path
    output_file = os.path.join(app.config['STATIC_FOLDER'], filename)

    # Define the preprocessing function
    def preprocess():
        available_voices = get_available_voices(language)
        if voice in available_voices:
            return voice
        else:
        # If the selected voice is not available, use the first available voice
            print('error detecting voice')
        return available_voices[0]


    # Create a gTTS object with the selected language and voice, and save the text as audio
    tts = gTTS(text=text, lang=language, tld='com', slow=False, pre_processor_funcs=[preprocess])
    tts.save(output_file)

    # Return the unique filename
    return filename



@app.route('/')
def index():
    languages = tts_langs()
    languages_dict = {lang_code: {'name': lang_name} for lang_code, lang_name in languages.items()}
    formats = list(app.config['AVAILABLE_FORMATS'])
    return render_template('index.html', languages=languages_dict, formats=formats, language="en")





@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    language = request.form['language']
    voice = request.form['voice']
    audio_format = request.form['format']

    if file and allowed_file(file.filename) and audio_format in app.config['AVAILABLE_FORMATS']:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        if filename.lower().endswith('.pdf'):
            # Convert PDF to text
            import textract
            text = textract.process(filepath).decode('utf-8')
        elif filename.lower().endswith('.docx'):
            # Convert Word document to text
            import docx2txt
            text = docx2txt.process(filepath)
        else:
            # Read text file
            with open(filepath, 'r') as f:
                text = f.read()

        # Generate output audio file and get the unique filename
        audio_filename = text_to_speech(text, language, voice, audio_format)

        return redirect(url_for('play_or_download', filename=audio_filename))

    else:
        return redirect(url_for('index'))


@app.route('/play_or_download/uploads/<filename>')
def play_or_download(filename):
    return render_template('play_or_download.html', filename=filename)


@app.route('/play/<filename>')
def play(filename):
    print('filename is', filename)
    return render_template('play.html', filename=filename)


@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run()
