import numpy as np
import matplotlib.pyplot as plt


time_step = 0.02
period = 5.
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2* np.pi/ period * time_vec) + 0.05 * np.random.randn(time_vec.size)
plt.figure(figsize=(6,5))
plt.plot(time_vec,sig)
plt.show()


# Real-World Use Cases
# Audio Engineering: Representing a voice recording with background wind noise or electrical "hum".

# Medical Monitoring: An raw ECG (heart monitor) signal that contains electrical interference from the hospital equipment.

# Industrial IoT: A vibration sensor on a turbine that captures the machine's "health" mixed with random environmental shaking.

# Communications: A Wi-Fi or 5G radio signal traveling through the air that picks up static before reaching your device.

# ----------------------------------------------------------------------------------------------------



import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

# 1. Create a signal with a specific frequency (e.g., 5 Hz)
time_step = 0.02
period = 5.0
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 * np.random.randn(time_vec.size)

# 2. Applying FFT (from your screenshot)
sample_freq = fftpack.fftfreq(sig.size, d=time_step)
sig_fft = fftpack.fft(sig)
power = np.abs(sig_fft) # Extract the magnitude

# 3. Plotting the results
plt.figure(figsize=(6, 5))
# We only plot the positive frequencies for clarity
plt.plot(sample_freq[sample_freq > 0], power[sample_freq > 0])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')
plt.title('FFT Analysis: Finding the Dominant Frequency')
plt.grid(True)
plt.show()


# Predictive Maintenance: Detecting if a factory motor is vibrating at a "danger" frequency before it breaks.

# Medical Diagnostics: Analyzing an ECG or EEG to find specific heart or brain wave patterns buried in electrical noise.

# Audio Recognition: Identifying a song or a voice command (like "Siri" or "Alexa") by looking at the frequency "fingerprint."

# Defense/Sonar: Identifying a submarine by the specific frequency of its propeller sounds.


# ----------------------------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

# --- PHASE 1: RE-CREATE THE NOISY SIGNAL ---
time_step = 0.02
time_vec = np.arange(0, 20, time_step)
# Pure 5Hz signal + random noise
sig = np.sin(2 * np.pi / 5.0 * time_vec) + 0.5 * np.random.randn(time_vec.size)

# --- PHASE 2: FFT & FILTERING (From your screenshot) ---
sig_fft = fftpack.fft(sig)
sample_freq = fftpack.fftfreq(sig.size, d=time_step)
power = np.abs(sig_fft)

# Find the peak frequency (the real signal)
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]

# Create a copy and remove high-frequency noise
high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0

# --- PHASE 3: IFFT (The Clean Signal) ---
filtered_sig = fftpack.ifft(high_freq_fft)

# --- VISUALIZATION ---
plt.figure(figsize=(10, 5))
plt.plot(time_vec, sig, label='Original (Noisy)', alpha=0.5)
plt.plot(time_vec, filtered_sig, linewidth=3, label='Filtered (Clean)', color='red')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.title("SciPy Signal Cleaning: Noise Removal via IFFT")
plt.show()



# The 3-Step Process
# FFT (Analyze): Breaks a messy signal down into its individual frequencies.

# Filter (Clean): Identifies the "noise" frequencies and sets them to zero.

# IFFT (Reconstruct): Turns the cleaned frequencies back into a smooth, usable signal.

# Real-World Examples
# Voice/Audio: Removing wind noise from phone calls or "hum" from music recordings.

# Medicine: Cleaning "fuzz" from heart monitors (ECG) or turning raw data into MRI images.

# Industry: Detecting engine failure by finding hidden vibration "peaks" that shouldn't be there.

# Internet: Combining thousands of frequencies into a single 5G or Wi-Fi signal.