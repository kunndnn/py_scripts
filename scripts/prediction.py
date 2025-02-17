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

    # Classify each segment and calculate confidence
    results = []
    for i, segment in enumerate(segments):
        # Save the segment temporarily (for debugging)
        segment_path = 'temp_segment.png'
        cv2.imwrite(segment_path, segment)

        # Extract features and classify
        features = extract_features(segment_path)
        prediction = model.predict([features])[0]  # Predict class (0 or 1)

        # Get probabilities for both classes (Roman and Gurmukhi)
        probabilities = model.predict_proba([features])[0]
        confidence = max(probabilities)  # Maximum confidence
        script = 'Roman' if prediction == 0 else 'Gurmukhi'

        # Print the prediction, confidence, and probabilities
        print(f"Segment {i}:")
        print(f" - Predicted: {script}")
        print(f" - Confidence: {confidence:.4f}")
        print(f" - Probabilities: {probabilities}")
        print(f"{script} this is the results till now !!!!!!!!!!!")

        results.append(script)

    # Summarize classification statistics
    unique_results = set(results)
    print("\n==== Classification Summary ====")
    for result in unique_results:
        count = results.count(result)
        print(f" - {result}: {count} segments classified")

    return results
