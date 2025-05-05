import time
import joblib
import platform
import numpy as np
from audio_utils import record_audio, extract_fft_features
import os
import sys

def resource_path(relative_path):
    """Get the absolute path to a resource bundled with the app."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load trained model using the correct path
model_path = resource_path("snap_model.pkl")
model = joblib.load(model_path)

def shutdown_computer():
    os_name = platform.system()
    if os_name == "Windows":
        os.system("shutdown /s /t 1")
    elif os_name == "Linux" or os_name == "Darwin":
        os.system("shutdown now")

# Silent Loop: Runs in the background without showing any windows
while True:
    try:
        audio = record_audio()
        features = extract_fft_features(audio)
        prediction = model.predict([features])[0]

        if prediction == 1:
            shutdown_computer()
            break

        time.sleep(1)  # Check every 0.5 seconds for a snap

    except Exception as e:
        pass  # Ignore any errors silently
