import cv2
from fer import FER

# Initialize detector
detector = FER(mtcnn=False)  # Use Haar cascade (no faceNet)

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions
    results = detector.detect_emotions(frame)

    # Draw results
    for result in results:
        (x, y, w, h) = result["box"]
        emotions = result["emotions"]
        top_emotion = max(emotions, key=emotions.get)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, top_emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

    # Show window
    cv2.imshow("CustomerConnect - Emotion Detection", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
