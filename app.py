from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Route to show form with a detected emotion
@app.route('/')
def home():
    detected_emotion = "Happy"  # You can update this with real-time emotion later
    return render_template('index.html', emotion=detected_emotion)

# Handle feedback submission
@app.route('/submit', methods=['POST'])
def submit():
    emotion = request.form['emotion']
    feedback = request.form['feedback']

    db_path = "database/feedback.db"
    abs_path = os.path.abspath(db_path)
    print(f"📂 Using database at: {abs_path}")

    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("INSERT INTO emotions (emotion, feedback) VALUES (?, ?)", (emotion, feedback))
        conn.commit()
        conn.close()
        return "✅ Feedback Submitted Successfully!"

    except sqlite3.OperationalError as e:
        return f"❌ Database error: {e}"

# Route to show feedback dashboard
@app.route('/dashboard')
def dashboard():
    db_path = "database/feedback.db"
    abs_path = os.path.abspath(db_path)
    print(f"📂 Loading dashboard from DB: {abs_path}")

    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM emotions ORDER BY timestamp DESC")
        rows = c.fetchall()
        conn.close()
        return render_template("dashboard.html", rows=rows)
    
    except sqlite3.OperationalError as e:
        return f"❌ Failed to load dashboard: {e}"

if __name__ == '__main__':
    app.run(debug=True)
