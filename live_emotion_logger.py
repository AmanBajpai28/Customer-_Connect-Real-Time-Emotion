import cv2
from fer import FER
import sqlite3
import time
import os

# Initialize FER detector
detector = FER()

# Setup database path
db_path = "database/feedback.db"
abs_path = os.path.abspath(db_path)
print(f"📂 Using database at: {abs_path}")

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Failed to open webcam.")
    exit()

print("🎥 Logging emotion... (Press 'q' to quit)")

last_logged_time = 0  # Time tracking for DB logging
label = ""  # To display on screen

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to capture frame")
            break

        # Detect emotion (every frame for display)
        result = detector.top_emotion(frame)
        if result:
            emotion, score = result
            label = f"{emotion} ({round(score, 2)})"
        else:
            label = "No emotion detected"

        # Show label on screen
        cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (0, 255, 0), 2, cv2.LINE_AA)

        # Show webcam window
        cv2.imshow("Emotion Logger (Press 'q' to quit)", frame)

        # Log to DB every 2 seconds
        current_time = time.time()
        if result and (current_time - last_logged_time >= 2):
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute("INSERT INTO emotions (emotion, feedback) VALUES (?, ?)",
                          (emotion, "Auto-Logged"))
                conn.commit()
                conn.close()
                print(f"😃 Detected Emotion: {label} ✅ Logged to DB")
            except Exception as e:
                print(f"❌ DB Error: {e}")
            last_logged_time = current_time

        # Break on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\n🛑 Interrupted by user")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("📷 Webcam closed.")
