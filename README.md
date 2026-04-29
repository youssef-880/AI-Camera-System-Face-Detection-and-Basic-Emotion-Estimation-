AI Camera System (Face Detection and Basic Emotion Estimation)

This project is a real-time webcam-based computer vision system that detects faces and estimates basic emotional states using simple image processing techniques. It is an improved and more stable version of the earlier implementation.

Use the following file to run the project:

ai_camera.py

This is the newer version of the system and should be used instead of any older files.

What the project does
Detects faces in real time using your webcam
Detects smiles inside the detected face region
Labels the face with a basic emotional state:
Happy (when a smile is detected)
Neutral (when no smile is detected)
Displays a simple on-screen interface with:
Face bounding boxes
Emotion label
FPS counter for performance monitoring
Tools and libraries used

This project is built using:

OpenCV (computer vision library cv2)
Used for webcam access, face detection, and drawing overlays on the video feed
Python standard library
Used for timing and FPS calculation

No machine learning frameworks or external AI models are required.

Requirements

To run this project, you need:

Python 3.11 recommended (tested and stable version)
OpenCV library
Installation

Install OpenCV using pip:

pip install opencv-python

How to run the project

Navigate to the project folder and run:

python ai_camera.py

To stop the program, press:

q

Notes
This is not a deep learning based emotion recognition system
Emotion detection is based on smile detection only and is therefore a simplified approximation
Performance and accuracy depend on lighting and camera quality
If the webcam does not open, change the video capture line to:

cv2.VideoCapture(0, cv2.CAP_DSHOW)

Why this version

This version is the cleaned and improved update of the earlier project. It fixes previous issues where distance from the camera incorrectly affected emotion detection. The logic is now more stable and consistent, and the overall structure is cleaner for future upgrades.

Future improvements

This project can be expanded into:

Real AI-based emotion recognition models
Hand gesture recognition
Face recognition for identifying specific users
Smart recording or alert systems based on detected states
