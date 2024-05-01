import webbrowser
from flask import Flask, render_template, request
import os
from main import process_video
import sys

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_video', methods=['POST'])
def process_video_route():
    file = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    # Call function to process video and save results
    results = process_video(file_path)
    # Write processing message to the result file
    write_processing_message(results)
    # Stop the Flask server
    sys.exit()
def write_processing_message(results):
    with open('test.csv', 'w') as f:
        f.write('Detection and extraction is completed. Output file named test.csv is created in the working directory.')

if __name__ == '__main__':
    # Open the browser automatically when the server starts
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)
