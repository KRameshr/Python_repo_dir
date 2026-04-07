
# Problem Statement:
#   You work in XYZ Company as a Python developer. The company officials want you to build a Python program. Tasks To Be Performed:

# 1. Load cars data as dataframe using pandas and create a bar plot between number of cylinders and frequency of cars with that many number of cylinders
# ● Set xlabel as Number of cylinders
# ● Set ylabel as Frequency of cars
# ● Draw a bar plot

# 2. Write code to load data from cars and print a bar graph of count of columns with null values.

# 3. Use the 'mpg' (Miles Per Gallon column) and draw a histogram:
# ● Set xlabel: Miles per gallon
# ● Set ylabel: Frequency
# ● Set title as Miles Per Gallon Histogram
# ● Use mpg column to generate a histogram

# 4. Draw a boxplot on the card dataframes hp column:
# ● Set xlabel: Car Horsepower
# ● Set title as Boxplot for car horsepower
# ● Use hp column to generate a boxplot



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mtcars.csv')
plt.figure(figsize=(8, 6))
cyl_counts = df['cyl'].value_counts().sort_index()


plt.bar(cyl_counts.index.astype(str), cyl_counts.values, color='skyblue', edgecolor='black')
plt.xlabel('Number of cylinders')    
plt.ylabel('Frequency of cars')   
plt.title('Cylinders Frequency')
plt.show()


null_counts = df.isnull().sum()
plt.bar(null_counts.index, null_counts.values, color='salmon', edgecolor='black')
plt.xlabel('Columns')
plt.ylabel('Count of Null Values')
plt.title('Null Values per Column')
plt.xticks(rotation=45) # Rotate names for readability
plt.show()


plt.hist(df['mpg'], bins=10, color='lightgreen', edgecolor='black')
plt.xlabel('Miles per gallon')      
plt.ylabel('Frequency')              
plt.title('Miles Per Gallon Histogram') 
plt.show()


plt.boxplot(df['hp'],vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.xlabel('Car Horsepower')         
plt.title('Boxplot for car horsepower') 
plt.show()