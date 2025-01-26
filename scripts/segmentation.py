import cv2
import numpy as np

def segment_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Threshold the image to binary
    _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    # Find contours (used to segment the words)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours based on their x-coordinate (left to right)
    contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

    words = []
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        # Crop the word from the image
        word = image[y:y+h, x:x+w]
        
        # Only add the word if its size is reasonable
        if word.shape[1] > 10 and word.shape[0] > 10:
            words.append(word)
    
    return words
