import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
from scipy.interpolate import interp1d

# 1. Your Original Data (Sparse points)
x = np.array([0.0, 0.5, 1.0, 1.5, 2.0])

# This is the function from your screenshot (inverted with -)
def f(x):
    return -np.exp(-(x-0.7)**2)

y = f(x)

# 2. Optimization: Find the exact minimum point
# minimize_scalar looks for the 'x' that results in the lowest 'y'
result = optimize.minimize_scalar(f)
x_min = result.x
y_min = f(x_min)

# 3. Interpolation: Create a smooth curve for plotting
# We use 'cubic' to make the line curve naturally through your 5 points
x_new = np.linspace(0, 2, 100)
f_interp = interp1d(x, y, kind='cubic')

# 4. Visualization
plt.figure(figsize=(10, 6))

# Plot original points
plt.plot(x, y, 'o', label='Original Data Points', markersize=8)

# Plot the smooth interpolated curve
plt.plot(x_new, f_interp(x_new), '-', label='Interpolated Curve (Cubic)')

# Highlight the Minimum Point found by optimize.minimize_scalar
plt.plot(x_min, y_min, 'r*', markersize=15, label=f'Found Min at x={x_min:.2f}')

plt.title('SciPy: Combining Interpolation & Optimization')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"The exact minimum is located at x = {x_min}")


