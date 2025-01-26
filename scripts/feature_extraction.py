import cv2
import numpy as np

def extract_features(image_path):
    # Read and preprocess image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale
    image = cv2.resize(image, (64, 64))  # Resize to 64x64
    features = image.flatten()  # Flatten image to 1D array
    return features