import matplotlib.pyplot as plt
import numpy as np

# Data: Most values are near 50, fewer at the edges
total = [45, 48, 50, 52, 55, 30, 70, 49, 51, 53, 47, 50]
#  list
order = [0, 20, 40, 60, 80, 100] 
discount = [30,40,50,60,10,30,45,60]

data = list([total, order, discount])
plt.boxplot(data, showmeans=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red', linewidth=2),
            meanprops=dict(marker='D', markeredgecolor='green', markerfacecolor='yellow'))


plt.title("Colored Boxplot with Mean")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()