import matplotlib.pyplot as plt
import numpy as np

# Data: Most values are near 50, fewer at the edges
total = [45, 48, 50, 52, 55, 30, 70, 49, 51, 53, 47, 50]
#  list
order = [0, 20, 40, 60, 80, 100] 
discount = [30,40,50,60,10,30,45,60]

data = list([total, order, discount])
parts = plt.violinplot(data, showmeans=True, showmedians=True)

colors = ['skyblue', 'lightgreen', 'tomato']
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

# 4. Styling the internal lines (Mean and Median)
parts['cmeans'].set_edgecolor('blue')
parts['cmedians'].set_edgecolor('red')

plt.title("Colored violinplot with Mean")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()