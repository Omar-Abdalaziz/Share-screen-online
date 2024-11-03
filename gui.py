# gui.py
import tkinter as tk
import threading
import webbrowser
import subprocess
import os

def start_server():
    # بدء تشغيل الخادم في عملية جديدة
    subprocess.Popen(['python', 'server.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)

def generate_link():
    link = "http://localhost:5000/video_feed"
    webbrowser.open(link)
    output_label.config(text=f"Session link: {link}")

# إنشاء واجهة المستخدم
app = tk.Tk()
app.title("Remote Access Session Generator")

start_button = tk.Button(app, text="Start Server", command=start_server)
start_button.pack(pady=10)

link_button = tk.Button(app, text="Generate Session Link", command=generate_link)
link_button.pack(pady=10)

output_label = tk.Label(app, text="")
output_label.pack(pady=10)

app.mainloop()
