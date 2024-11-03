# server.py
from flask import Flask, Response, render_template_string
import pyautogui
import cv2
import numpy as np

app = Flask(__name__)

def generate_frames():
    while True:
        # التقاط الشاشة
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # تشفير الصورة كجسيم بت
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # إرسال الصورة كإطار HTTP
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    # صفحة HTML الرئيسية مع CSS لتنسيق العرض
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Remote Session Viewer</title>
        <style>
            body {
                background-color: #f8f9fa;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            h1 {
                color: #343a40;
            }
            .video-container {
                border: 5px solid #007bff;
                border-radius: 10px;
                overflow: hidden;
            }
            img {
                width: 100%;
                height: auto;
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="video-container">
            <h1>Remote Session Viewer</h1>
            <img src="{{ url_for('video_feed') }}">
        </div>
    </body>
    </html>
    ''')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
