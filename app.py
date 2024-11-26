from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Ensure the uploads folder exists
uploads_dir = 'uploads'
os.makedirs(uploads_dir, exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    # Save the file to the uploads folder
    file_path = os.path.join(uploads_dir, file.filename)
    file.save(file_path)
    
    # Here, you would call your face and eye detection function
    # For demonstration, we'll just simulate a result
    result = "Face detected, eye contact maintained."  # Replace with actual detection result
    
    return render_template('result.html', filename=file_path, result=result)

if __name__ == '__main__':
    app.run(debug=True)
