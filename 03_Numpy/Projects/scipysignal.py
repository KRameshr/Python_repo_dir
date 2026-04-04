import matplotlib.pyplot as plt
import numpy as np
# from scipy import signal

# # 1. Create a high-resolution signal (200 data points)
# t = np.linspace(-10, 10, 200) # Defining Time Interval between -10 and 10 seconds with 200 points
# y = np.sin(t)                 # A standard sine wave

# # 2. Resample the signal down to 100 points
# # signal.resample uses Fourier transform (FFT) for high accuracy
# x_resampled = signal.resample(y, 100) 

# # 3. Visualization
# plt.plot(t, y) 
# # Plot resampled points as dots to see the difference
# plt.plot(t[::2], x_resampled, 'o', label='Resampled (100 pts)', markersize=4)

# plt.title("Signal Resampling: Reducing Data Density")
# plt.legend()
# plt.show()

x = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
def f(x):
    return np.exp(-(x-0.7)**2)
plt.plot(x, f(x), 'o-', label='Original Data') 
