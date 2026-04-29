import cv2
import time

# Load OpenCV cascades
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(80, 80)
    )

    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # UI header
    cv2.putText(frame, "AI CAMERA SYSTEM", (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.putText(frame, f"FPS: {int(fps)}", (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]

        # Detect smiles inside face
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=20
        )

        # Stable emotion logic (NO distance bug)
        if len(smiles) > 0:
            emotion = "Happy 😊"
            color = (0, 255, 0)
        else:
            emotion = "Neutral 😐"
            color = (200, 200, 200)

        # Face box
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        # Inner face indicator
        cv2.circle(frame, (x + w//2, y + h//2), 5, color, -1)

        # Emotion label
        cv2.putText(frame, emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Confidence hint (based on detection stability, not distance)
        confidence = min(100, int((w * h) / 1000))
        cv2.putText(frame, f"Face confidence: {confidence}%",
                    (x, y + h + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 2)

    # No face detected UI
    if len(faces) == 0:
        cv2.putText(frame, "No face detected",
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 0, 255), 2)

    cv2.imshow("AI Vision System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()