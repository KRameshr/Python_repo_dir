import pandas as pd
import matplotlib.pyplot as plt

#  Import the cars.csv file

df = pd.read_excel('somecars1.xlsx')

# 1. Generate the line plot
plt.figure(figsize=(10, 5))

# We use df.index to represent the 'model' rows since they aren't named in the data
plt.plot(df.index, df['hp'], marker='o', color='red', linestyle='-')

#  Setting the specific labels and title as requested
plt.xlabel('Models of the cars')      # x-axis label
plt.ylabel('Horse-Power of Cars')     # y-axis label
plt.title('Model Names vs HorsePower') # Title

# Optional: Add a grid for better readability
plt.grid(True, linestyle=':', alpha=0.7)

plt.show()


# 2. Generate the bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['carb'], df['gear'], color='orange')

#  Apply the requested labels and title
plt.xlabel('Number of carburetors')       # x-axis label
plt.ylabel('Number of forward gears')    # y-axis label
plt.title('carbs vs gear')               # Title

# Optional: Add a grid for better scale reading
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


# 3. Plot the histogram for the 'wt' column
plt.figure(figsize=(10, 6))
plt.hist(df['wt'], bins=30, color='skyblue', edgecolor='black')

#  Add the requested labels and title
plt.xlabel('weight of the cars')           # x-axis label
plt.ylabel('Count')                        # y-axis label
plt.title('Histogram for the weight values') # Title

# Show the plot
plt.show()



# 4. Plot the histogram for the 'wt' column

df = pd.read_csv('mtcars.csv')


# 2. Prepare the data
# Pie charts can get crowded with many rows, so we will plot the first 7 models
df_subset = df.head(14)

plt.figure(figsize=(10, 6))
plt.pie(df_subset['cyl'],
        labels=df_subset['model'], 
        autopct='%1.1f%%',     # Show percentage on each slice
        startangle=140,        # Rotate the start for better visual
        colors=plt.cm.Paired.colors) # Use a professional color palette)

#  Add the requested labels and title
plt.title('Cylinder Proportions by Car Model')

# Show the plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
customer = pd.read_excel("somecars1.xlsx")

# 2. Sort the data by 'am' so the area fills correctly from left to right
customer_sorted = customer.sort_values('am')

# 3. Create the Area Chart
plt.figure(figsize=(10, 6))
plt.fill_between(customer_sorted['am'], customer_sorted['carb'], color="skyblue", alpha=0.4)
plt.plot(customer_sorted['am'], customer_sorted['carb'], color="Slateblue", alpha=0.6, linewidth=2)

# 4. Set Labels and Title as requested
plt.xlabel('Transmission')
plt.ylabel('Number of carburetors')
plt.title('Transmission vs Number of carburetors')

# Optional: Make the x-axis labels clearer
plt.xticks([0, 1], ['0 (Automatic)', '1 (Manual)'])

plt.show()