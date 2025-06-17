import tkinter as tk
from tkinter import messagebox
import requests
import subprocess
import sys
import os

LOCAL_VERSION = "2.0"
VERSION_FILE_URL = "https://raw.githubusercontent.com/someless/tk-updater/main/version.txt"

def check_for_update():
    try:
        response = requests.get(VERSION_FILE_URL, timeout=5)
        response.raise_for_status()
        latest_version = response.text.strip()

        if latest_version != LOCAL_VERSION:
            result = messagebox.askyesno("Update Available",
                f"A new version ({latest_version}) is available!\n\nYou are using version {LOCAL_VERSION}.\n\nDo you want to update now?")
            if result:
                subprocess.Popen([sys.executable, "updater.py"])
                root.destroy()
    except Exception as e:
        print("Update check failed:", e)

# ------------------------- Tkinter UI ----------------------------
root = tk.Tk()
root.title("My App v2.0")
root.geometry("300x150")

label = tk.Label(root, text="Welcome to My App v2.0")
label.pack(pady=20)

btn = tk.Button(root, text="Check for Update", command=check_for_update)
btn.pack()

root.mainloop()
