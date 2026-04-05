import pandas as pd
import matplotlib.pyplot as plt

# 1. You must LOAD the data in THIS file
cars = pd.read_excel("final_car_clusters.xlsx")

# 2. Now you can define your variables
y1 = cars['hp']
x = range(len(cars))

# 3. Create the plot
plt.plot(x, y1, color='blue', marker='o')

# 4. Add labels (Optional but professional)
plt.title("Car Horsepower")
plt.xlabel("Car Index")
plt.ylabel("HP")

# 5. Display the window
plt.show()

y1 = cars['cyl']
# 3. Create the plot
plt.plot(x, y1, color='blue', marker='o')

# 4. Add labels (Optional but professional)
plt.title("Car cyl")
plt.xlabel("Car cyl")
plt.ylabel("cyl")

# 5. Display the window
plt.show()


# 2. Assign values
y1 = cars['cyl']
y2 = cars['disp']
x = range(len(cars))

# 3. Plot with 'label' arguments (Crucial for the legend)
plt.plot(x, y1, color='blue', marker='o', label='Cylinders')
plt.plot(x, y2, color='red', marker='o', label='Displacement')

# 4. Add the Legend and Labels
plt.legend(loc='upper right') # Now this knows what to show!
plt.title('Engine Comparison: Cylinders vs Displacement')
plt.xlabel('Car Index')
plt.ylabel('Values')

# 5. Display
plt.show()


#  area plot

# 2. Create the Area Plot
plt.figure(figsize=(10, 6))
# use fill_between for the area effect
y1 = cars['cyl']
y2 = cars['mpg']
# alpha=0.4 makes the colors see-through so they can overlap
plt.fill_between(x, y1, color="blue", alpha=0.4, label='Cylinders')
plt.fill_between(x, y2, color="green", alpha=0.4, label='Displacement')

# 3. Add the outlines (Optional, but makes it look sharper)
plt.plot(x, y1, color="purple", linewidth=1)
plt.plot(x, y2, color="black", linewidth=1)

# 4. Add the Legend and Labels
plt.legend(loc='upper right')
plt.title('Engine Comparison: Cylinders vs Displacement (Area Plot)')
plt.xlabel('Car Index')
plt.ylabel('Values')

# 5. Display
plt.show()

#  area line plot

x = range(len(cars))
y1 = cars['cyl']
y2 = cars['mpg']

plt.figure(figsize=(10, 6))

# --- AREA PART ---
# We use alpha=0.3 for a soft background fill
plt.fill_between(x, y1, color="blue", alpha=0.3, label='Cylinders')
plt.fill_between(x, y2, color="green", alpha=0.3, label='MPG')

# --- LINE PART ---
# We plot the lines on top to make the edges "sharp"
plt.plot(x, y1, color="blue", linewidth=2, marker='o', markersize=4)
plt.plot(x, y2, color="green", linewidth=2, marker='s', markersize=4)

# 4. Add the Legend and Labels
plt.legend(loc='upper right')
plt.title('Performance Analysis: Cylinders vs MPG', fontsize=14)
plt.xlabel('Car Index')
plt.ylabel('Value')
plt.grid(axis='y', linestyle='--', alpha=0.5) # Adds a clean background grid

# 5. Display
plt.show()

#  Create the Bar Plot

# 2. Sort the data by MPG (Highest to Lowest)
# This makes the chart much easier to read than a random order
cars_sorted = cars.sort_values(by='mpg', ascending=False)

# 3. Create the Bar Plot
plt.figure(figsize=(12, 6))
plt.bar(cars_sorted.index, cars_sorted['mpg'], color='skyblue', edgecolor='navy')

# 4. Design and Labels
plt.title('Car Fuel Efficiency: Miles Per Gallon (Sorted)', fontsize=16)
plt.xlabel('Car Models', fontsize=12)
plt.ylabel('MPG', fontsize=12)
plt.xticks(rotation=90) # Rotate labels so they don't overlap
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add horizontal grid lines

# 5. Show
plt.tight_layout() # Ensures labels are not cut off
plt.show()

# Create the Har Bar Plot
# 2. Sort by MPG (Highest at the top)
# We use ascending=True because in a horizontal plot, the last items appear at the top
cars_sorted = cars.sort_values(by='mpg', ascending=True)

# 3. Create the Horizontal Plot
plt.figure(figsize=(10, 8))

# Note: plt.barh uses (y, width) instead of (x, height)
plt.barh(cars_sorted.index, cars_sorted['mpg'], color='teal', edgecolor='black')

# 4. Design and Labels
plt.title('Fuel Efficiency: Miles Per Gallon (Horizontal)', fontsize=16)
plt.xlabel('Miles Per Gallon (MPG)', fontsize=12)
plt.ylabel('Car Models', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6) # Grid lines now run vertically

# 5. Display
plt.tight_layout()
plt.show()