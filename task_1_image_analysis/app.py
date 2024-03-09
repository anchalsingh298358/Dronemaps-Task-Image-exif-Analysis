# app.py
from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import csv

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def analyze_image(image_path):
    global metadata
    global violation_flag
    metadata = {}
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    metadata[tag] = value
            height = metadata.get(256, 0)
            speed = metadata.get(106, 0)  # Assuming speed is stored in tag 106, adjust according to your image data
            violation_flag = height > 60 or speed > 5
            return metadata, violation_flag
    except Exception as e:
        print("Error analyzing image:", e)
        return None, False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', message='No selected file')

    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        metadata, violation_flag = analyze_image(file_path)

        return render_template('result.html', filename=filename, metadata=metadata, violation_flag=violation_flag)

    else:
        return render_template('index.html', message='Invalid file format')

@app.route('/download_report/<filename>', methods=['GET'])
def download_report(filename):
    report_filename = f"{filename.split('.')[0]}_report.csv"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], report_filename)

    with open(file_path, mode='w', newline='') as csvfile:
        fieldnames = ['Tag', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for tag, value in metadata.items():
            writer.writerow({'Tag': tag, 'Value': value})
        
        writer.writerow({'Tag': 'Violation Flag', 'Value': violation_flag})

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)