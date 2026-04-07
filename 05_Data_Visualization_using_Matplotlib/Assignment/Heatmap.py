import seaborn as sns
import matplotlib.pyplot as plt

# 1. Define the 2D Data (Matrix)
data = [
    [99, 85, 15],
    [78, 5, 25],
    [90, 45, 35]
]

# 2. Create the Heatmap
# annot=True puts the actual numbers inside the boxes
sns.heatmap(data, annot=True, cmap="YlGnBu") 

# 3. Final Touch
plt.title("Intensity Heatmap")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# 1. View a built-in palette (like 'viridis' or 'magma')
palette = sns.color_palette("magma", 10) # Get 10 colors from magma
sns.palplot(palette)

# 2. View a custom list of colors
my_colors = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.palplot(my_colors)

plt.show()