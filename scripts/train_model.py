import os
import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Function to load and preprocess images
def load_data(data_dir):
    X = []
    y = []
    for label, script in enumerate(['Roman', 'Gurmukhi']):
        script_dir = os.path.join(data_dir, script)
        for image_name in os.listdir(script_dir):
            image_path = os.path.join(script_dir, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale
            if image is None:
                print(f"Warning: Could not read image {image_path}. Skipping.")
                continue
            image = cv2.resize(image, (64, 64))  # Resize to 64x64
            X.append(image.flatten())  # Flatten image to 1D array
            y.append(label)  # Assign label (0 for Roman, 1 for Gurmukhi)
    return np.array(X), np.array(y)

# Main script
if __name__ == '__main__':
    # Load data
    data_dir = 'data'  # Folder containing 'Roman' and 'Gurmukhi' subfolders
    if not os.path.exists(data_dir):
        print(f"Error: Data directory '{data_dir}' does not exist.")
        exit(1)

    X, y = load_data(data_dir)

    # Check if data was loaded
    if len(X) == 0 or len(y) == 0:
        print("Error: No data found. Ensure images are in 'data/Roman' and 'data/Gurmukhi' folders.")
        exit(1)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train SVM model
    model = SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    # Save model
    model_path = 'model.pkl'
    joblib.dump(model, model_path)
    print(f"Model saved as {model_path}")