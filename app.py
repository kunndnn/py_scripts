import sys
import os
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
    result = None
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', error="No file uploaded!")
        
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No file selected!")
        
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Classify the image
        try:
            result = classify_word_image(file_path)
        except Exception as e:
            return render_template('index.html', error=f"Error processing image: {str(e)}")
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)