import matplotlib.pyplot as plt
import numpy as np

# Data: Most values are near 50, fewer at the edges
a = [45, 48, 50, 52, 55, 30, 70, 49, 51, 53, 47, 50]
# range of interval b/w 10-20
b = [0, 20, 40, 60, 80, 100]

plt.hist(a, bins=b, color='Red', edgecolor='black', alpha=0.8)


plt.title("Histogram Distribution")
plt.xlabel("Range (Bins)")
plt.ylabel("Frequency (Count)")
plt.grid(axis='x', linestyle='-', alpha=1) 
plt.grid(axis='y', linestyle='-', alpha=1) 
plt.savefig("Histgram.png")
plt.show()