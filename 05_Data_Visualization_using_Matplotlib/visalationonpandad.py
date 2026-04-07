# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

# customer = pd.read_excel("somecars1.xlsx")
# print(customer.head())



# print(customer['disp'].value_counts())
# print(customer['drat'].value_counts().keys().tolist(),customer['drat'].value_counts().tolist())
# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# # 1. Load your LOCAL file with Pandas
# customer = pd.read_excel("somecars1.xlsx")

# # 2. Set the "Aesthetic" (The Seaborn Magic)
# sns.set_theme(style="whitegrid")

# # 3. Create a plot using the Pandas DataFrame
# # Let's see how Displacement (disp) affects Miles Per Gallon (mpg)
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=customer, x="disp", y="mpg", hue="cyl", palette="viridis")

# plt.title("Car Data: Displacement vs. MPG")
# plt.show()



# 1. Load Data
customer = pd.read_excel("somecars1.xlsx")

# 2. Set the "Aesthetic"
sns.set_theme(style="whitegrid")

# 3. Create a Figure with 2 Subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# --- Plot 1: Scatter Plot (Numerical vs Numerical) ---
sns.scatterplot(data=customer, x="disp", y="mpg", hue="cyl", palette="viridis", ax=ax1)
ax1.set_title("Engine Size vs. Fuel Efficiency")

# --- Plot 2: Count Plot (Categorical Counting) ---
# We use 'cyl' because 'class' is not in your data
sns.countplot(data=customer, x="cyl", palette="magma", ax=ax2)
ax2.set_title("Frequency of Cylinder Types")

# 4. Final Polish
plt.tight_layout() # Prevents titles from overlapping
plt.show()


# 2. Set the style
sns.set_theme(style="whitegrid")

# 3. Create the Countplot
plt.figure(figsize=(8, 5))

# We use 'cyl' because it's a category in your data (4, 6, or 8)
sns.countplot(data=customer, x="cyl", palette="viridis")

# 4. Add labels
plt.title("Number of Cars by Cylinder Count", fontsize=14)
plt.xlabel("Cylinders (cyl)")
plt.ylabel("Count of Cars")

plt.show()