import sys
import os
import base64
from flask import Flask, request, render_template

# Add the scripts folder to the Python path
scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')
sys.path.append(scripts_dir)

# Import the prediction module
try:
    from prediction import classify_word_image
except ImportError as e:
    print(f"Error importing prediction module: {e}")
    print(f"Python path: {sys.path}")
    raise

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])



@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    image_data = None  

    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file uploaded!")

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error="No file selected!")

        # Save the file temporarily
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Read file as base64 buffer for preview
        with open(file_path, "rb") as img_file:
            image_data = base64.b64encode(img_file.read()).decode('utf-8')

        # Classify the image using the saved file path
        try:
            results = classify_word_image(file_path)
            results = list(set(results))
        except Exception as e:
            return render_template('index.html', error=f"Error processing image: {str(e)}")

    return render_template("index.html", results=results, image_data=image_data)

if __name__ == '__main__':
    app.run(debug=True)
