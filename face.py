import cv2
import os
from fer import FER  # Facial expression recognition

# Initialize webcam (0 is the default webcam)
cap = cv2.VideoCapture(0)

# Get the directory of the current Python file (main file)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the Haar Cascade XML file inside the 'models' folder
cascade_path = os.path.join(base_dir, "models", "haarcascade_frontalface_default.xml")

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cascade_path)

# Check if the Haar Cascade is loaded properly
if face_cascade.empty():
    print("Error loading cascade classifier. Check the file path.")
    cap.release()
    cv2.destroyAllWindows()
    exit()  # Exit the program if the classifier isn't loaded
else:
    print("Cascade classifier loaded successfully.")

# Initialize the emotion detector using FER
emotion_detector = FER()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame from webcam.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    # Draw rectangle around faces and detect expressions
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Crop the face area for emotion detection
        face_region = frame[y : y + h, x : x + w]

        # Detect emotions in the face region
        emotions = emotion_detector.detect_emotions(face_region)

        if emotions:
            # Get the most dominant emotion for the detected face
            dominant_emotion = emotions[0]["emotions"]
            detected_emotion = max(dominant_emotion, key=dominant_emotion.get)
            print(f"Detected emotion: {detected_emotion}")

            # Display the emotion text on the frame
            cv2.putText(
                frame,
                detected_emotion,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2,
            )

    # Display the resulting frame
    cv2.imshow("Face & Emotion Detection", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
