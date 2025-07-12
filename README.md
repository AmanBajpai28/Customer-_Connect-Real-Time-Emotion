
# 😊 Customer Connect: Real-Time Emotion Analysis

A Python-based real-time emotion detection system that uses a webcam to capture a user's facial expressions, detects their emotion using the `FER` (Facial Expression Recognition) library, and logs it to a SQLite database for analysis.

---

## 📌 Features

- Real-time emotion detection using webcam
- Face-based emotion recognition (Happy, Sad, Angry, etc.)
- Emotion logging with timestamp to a local SQLite database
- Displays live camera preview with detected emotion label
- Auto logs data every 2 seconds
- Easy to run via command line or VS Code terminal

---

## 🖼️ Preview

![App Screenshot](screenshot.png) <!-- Optional: add your own screenshot -->

---

## 🛠️ Technologies Used

- Python 3.x
- OpenCV
- FER (Facial Expression Recognition)
- TensorFlow / Keras (used internally by FER)
- SQLite (for database logging)

---

## 📂 Project Structure

```
Customer_Connect Real Time Emotion/
│
├── database/
│   └── feedback.db             # SQLite database file
│
├── live_emotion_logger.py     # Main script
├── test_camera.py             # Optional: for webcam testing
├── .gitignore                 # Ignore unnecessary files for Git
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies (optional)
```

---

## ▶️ How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/emotion-logger.git
cd "Customer_Connect Real Time Emotion"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install opencv-python==4.8.0.76 fer numpy
```

### 3. Run the Emotion Logger
```bash
python live_emotion_logger.py
```

Press **`q`** to exit the camera window.

---

## 📈 Emotion Logging

Each detected emotion is stored in `database/feedback.db` under the `emotions` table:

| id | emotion | feedback     | timestamp |
|----|---------|--------------|-----------|
| 1  | happy   | Auto-Logged  | 12:00:21  |
| 2  | neutral | Auto-Logged  | 12:00:23  |

---

## 📦 Optional Enhancements

- ✅ Add face bounding box with emotion label
- 📊 Create dashboard using Streamlit or Flask
- 💾 Export data to CSV for analysis
- 🌐 Convert to Web App using Flask
- 🧊 Package to `.exe` using PyInstaller

---

## 🙌 Author

**Aman Bajpai**  
AIML Co-Lead, Google Developer Groups - NIET  
[LinkedIn](https://www.linkedin.com/in/aman-bajpai-651a87266/) • [GitHub](https://github.com/AmanBajpai28)

---


