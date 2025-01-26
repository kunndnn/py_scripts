import joblib
from feature_extraction import extract_features

def classify_word_image(image_path):
    # Load trained model
    model = joblib.load('model.pkl')

    # Extract features from the image
    features = extract_features(image_path)

    # Predict script
    prediction = model.predict([features])[0]  # Predict class (0 or 1)
    script = 'Roman' if prediction == 0 else 'Gurmukhi'
    return script