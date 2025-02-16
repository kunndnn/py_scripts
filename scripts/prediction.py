import joblib
import os
import cv2
from feature_extraction import extract_features, segment_image
def classify_word_image(image_path):
    # Load trained model
    model_path = 'model.pkl'
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file '{model_path}' not found. Please train the model first.")

    model = joblib.load(model_path)

    # Segment the image into individual words/characters
    segments = segment_image(image_path)

    # Classify each segment
    results = []
    for segment in segments:
        # Save the segment temporarily (for debugging)
        segment_path = 'temp_segment.png'
        cv2.imwrite(segment_path, segment)

        # Extract features and classify
        features = extract_features(segment_path)
        prediction = model.predict([features])[0]  # Predict class (0 or 1)
        script = 'Roman' if prediction == 0 else 'Gurmukhi'
        results.append(script)

    return results