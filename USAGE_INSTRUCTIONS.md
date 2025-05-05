# 🛠 How to Use Snap-to-Shutdown on Your PC or Laptop

Welcome to the Snap-to-Shutdown project! This guide will walk you through the steps to install, run, and auto-start the Snap-to-Shutdown program, which listens for the sound of a finger snap and shuts down your PC instantly.
This program works silently in the background and has no visible interface, making it a seamless and fun automation tool for your computer.
---

### 📁 Step 1: Folder Setup

Make sure all the following files are in the same folder:
- `main.py`
- `audio_utils.py`
- `snap_model.pkl`

---

### ⚙️ Step 2: Install Required Libraries

Open a terminal (PowerShell or CMD) and run:

```bash
pip install numpy sounddevice scipy joblib scikit-learn
```

### 🧪 Step 3: Test the Script (Optional)
Once you have installed the dependencies, you can test if everything is working properly by running the script directly from your terminal. In the terminal, navigate to the folder containing your files and run
Run it to see if everything works:

```bash
python main.py
```
What to expect:
  The program will run silently in the background.
  If a finger snap is detected, the PC will immediately shut down.
  You won't see any window or notification while it’s running.

---

### 🧊 Step 4: Build the EXE
Now, let’s convert the Python script into an executable (.exe) file. This step is important because it will allow you to run the program on a Windows PC without needing Python installed.

To do this, use PyInstaller:
Open your terminal and navigate to the folder containing your files.

Run the following command:

```bash
python -m PyInstaller --onefile --noconsole --add-data "snap_model.pkl;." --hidden-import=sklearn --hidden-import=sklearn.ensemble._forest --hidden-import=sklearn.tree._tree main.py
```
What happens:
This command will create an executable (main.exe) in the dist/ folder.
The --noconsole flag ensures that the program runs silently without showing a terminal window.

---

### 🧍 Step 5: Run the Executable
Once the executable file (main.exe) is built, you can run it like any other application:

  1. Go to the dist/ folder.
  2. Double-click main.exe to launch it.
  3. The program will start running silently in the background, waiting for a finger snap.

### 🚀 Step 6: Auto-Start on Boot (Optional)
If you want the program to run automatically every time you start your PC, you can set it to auto-start with Windows.

Here’s how:

  1. Press Win + R to open the "Run" dialog.
  2. Type shell:startup and press Enter. This will open the Startup folder.
  3. Copy your main.exe file from the dist/ folder and paste it into the Startup folder.

     Now, every time you log into Windows, the program will start automatically in the background, ready to shut down your PC when a finger snap is detected.

---

### 🧯 How to Stop the Program
If you need to stop the program, follow these steps:

  1. Open Task Manager (Press Ctrl + Shift + Esc).
  2. In the "Processes" tab, find main.exe under background processes.
  3.   Right-click on main.exe and click End Task to stop the program.

This will immediately stop the program from running and prevent further shutdowns.



     
