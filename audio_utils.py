import numpy as np
import sounddevice as sd
from scipy.fft import fft

DURATION = 1  # Record for 1 second
SAMPLE_RATE = 44100

def record_audio():
    print("Listening for 1 second...")
    audio = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='float64')
    sd.wait()  # Wait until recording is finished
    return audio.flatten()

def extract_fft_features(audio):
    fft_vals = np.abs(fft(audio))
    return fft_vals[:500]  # Take first 500 frequency values
