import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
import datetime
import time

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'md'}  # Server code to make sure it doesn't happen.

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def store_file_details(fName, title, upload_time):
    # Using a file to store the file details because well,
    # Using a database makes my website vulnerable to the SQL injection attacks
    # Also, this is a simple app, so, I thought, this'd be better!..
    with open('files.txt', 'a+') as f:
        f.write(f'["{upload_time}", "{fName}", "{title}"]' + '\n')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['fileName']
        if file and allowed_file(file.filename):
            file_title = request.form['file_title']
            upload_time = str(time.time())
            filename = secure_filename(file.filename)
            store_file_details(filename, file_title, upload_time)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], upload_time.replace(" ", "")+'-'+filename))
            return redirect(url_for('index'))
    return render_template('upload.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    filename = filename.replace(' ', '')
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/static/<filename>')
def static_file(filename):
    return send_from_directory('static', filename)


@app.route('/')
def index():
    with open('files.txt') as f:
        files = f.readlines()
    files = list(map(eval, files))
    return render_template('index.html', files=files)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
