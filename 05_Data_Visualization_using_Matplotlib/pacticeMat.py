import numpy as np
import matplotlib.pyplot as plt

# 1. Dataset
x = np.arange(0, 10, 0.1)
y = 2 * x + 5

# 2. Setup Canvas FIRST
# This ensures all following commands apply to this specific window
plt.figure(figsize=(10, 5))

# 3. Plotting with Styles
# marker='o' with 0.1 increments creates a very dense line of dots!
plt.plot(x, y, label='y = 2x + 5', color='blue', linewidth=1.0, 
         linestyle=":", alpha=0.5, marker="o")

# 4. Customization
plt.title("Linear Function Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)

# 5. Legend Logic
# Since you defined 'label' in plt.plot, plt.legend() will find it automatically.
plt.legend(loc='best')

# 6. Show
plt.show()




# Displaying the both

x= np.arange(0,10,1)
y1 = 2*x + 5;
y2 = 3*x + 10;

plt.subplot(2,1,1)
plt.plot(x,y1)
plt.title("Graph1")

plt.subplot(2,1,2)
plt.plot(x,y2)
plt.title("Graph2")
plt.show()







