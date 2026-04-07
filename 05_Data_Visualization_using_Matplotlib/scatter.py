import numpy as np
import matplotlib.pyplot as plt

# 1. Dataset
a = [10, 20,30,40,50,60,70]
b = [5,3,2,5,6,7,1]
x = [1, 2,3,4,3,6,7]

plt.scatter(a, b,  color='blue', linewidth=1.0, linestyle=":", alpha=1, marker="o")
plt.scatter(a, x,  color='red', linewidth=1.0, linestyle=":", alpha=1, marker="o")
plt.scatter(b, x,  color='green', linewidth=1.0, linestyle=":", alpha=1, marker="o")



# 4. Customization
plt.title("Linear Function Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.savefig("Scatter.png")

# 5. Legend Logic
# Since you defined 'label' in plt.plot, plt.legend() will find it automatically.
plt.legend(['b','a','x'],loc='best')

# 6. Show
plt.show()