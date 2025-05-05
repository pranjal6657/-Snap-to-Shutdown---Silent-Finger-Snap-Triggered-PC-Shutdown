# 🔇 Snap-to-Shutdown - Silent Finger Snap Triggered PC Shutdown
A Python-based program that listens for the sound of a **finger snap** and instantly shuts down your PC when detected — running completely in the **background** with **no visible interface**.

![Snap-to-Shutdown Logo](Logo.png)
---

## 🚀 Features
- 🔊 Sound recognition using a trained ML model
- 🖐️ Detects finger snaps only — ignores other sounds
- 💻 Shuts down PC instantly upon detection
- 🧊 Runs silently with no open window (`--noconsole`)
- 🧠 Built using `scikit-learn`, `joblib`, `numpy`, and custom audio utilities
- ✅ Packaged as a `.exe` for Windows (works on laptops and desktops)

---

## 📦 Files Included
- `main.py` - main program loop
- `audio_utils.py` - handles audio recording & feature extraction
- `snap_model.pkl` - pre-trained ML model for detecting finger snaps

---

## 💡 Why This Project is Important
- **Demonstrates practical use of ML for sound classification**
- Shows how to run Python automation silently in background
- Could be extended for other smart triggers (like claps, phrases, etc.)
- A fun but powerful way to understand PyInstaller, joblib, and more

---

## 🧪 How It Works
1. The app constantly records short clips of audio.
2. Extracts frequency-domain features using FFT.
3. Uses a trained ML model to detect whether the sound is a finger snap.
4. If yes — initiates system shutdown.

---

## 📜 License
MIT License. Use at your own risk. Shutting down PCs forcefully may cause data loss.

---

## 🙌 Contribute
Want to improve this? Fork it, add features like:
- Voice confirmation before shutdown
- GUI to toggle listening on/off
- Shutdown timer or scheduling

Pull requests welcome!

---

## 📂 See `USAGE_INSTRUCTIONS.txt` to learn how to run it on your PC.
