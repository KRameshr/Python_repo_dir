import pandas as pd

# 1. Load the dataset
cars = pd.read_excel("final_car_clusters.xlsx")

# 2. Display the first 5 rows to verify it loaded correctly
print("--- First 5 Rows ---")
print(cars.head())


print("--- Last 5 Rows ---")
print(cars.tail())

print("--- Last 4 Rows ---")
print(cars.tail(4))


print("--- type ---")
print(type(cars))

# 3. Check the data types and column names
print("\n--- Data Information ---")
print(cars.info())



print("\n--- Data shape ---")
print(cars.shape)


# 4. Basic Statistics (Mean, Min, Max, etc.)
print("\n--- Descriptive Statistics ---")
print(cars.describe())


print("\n--- Descriptive mean ---")
print(cars.mean())

print("\n--- Descriptive median ---")
print(cars.median())

print("\n--- Descriptive std ---")
print(cars.std())

print("\n--- Descriptive max ---")
print(cars.max())

print("\n--- Descriptive min ---")
print(cars.min())

print("\n--- Descriptive count ---")
print(cars.count())


print("\n--- Descriptive describe ---")
print(cars.describe())

# cleaning 

# rename
# cars = cars.rename(columns={"Unnamed: 1":"model"})
# print(cars)

# # null values
# cars['qsec'] = cars['qsec'].fillna(cars['qsec'].mean())

# print("--- Data after filling qsec NaNs ---")
# print(cars['qsec'].head())

# Dropping 'qsec' and 'Unnamed: 0' (often found in Excel exports)
# unwanted = ["s.No"]
# cars = cars.drop(columns=unwanted)

# print(cars)


# cars.mpg = cars.mpg.astype(float)
# print(cars.info(show_counts=True))


# manupulatin 
print(cars.iloc[:,3]) 
print(cars.iloc[0:5,3])  
print(cars.iloc[:,:])  
print(cars.iloc[6:,4:])  
# all in 3 clo
print(cars.iloc[ :,3])  
print(cars.loc[ :,"gear"]) 
# up to 6 row in gear col 
print(cars.loc[ :6,"gear"])   
# up to 6 row in gear  to carb col 
print(cars.loc[ :6,"gear":"carb"])  

# set the value  enter col
cars["gear"] = 1
cars["cluster_group"] = 15
print(cars) 

#  increase the col
f = lambda x: x**2
cars["cluster_group"] = cars["cluster_group"].apply(f)
print(cars)

#  asc the col

cars.sort_values(by="wt")
print(cars)

#  asc the col

cars.sort_values(by="hp" ,ascending=False)
print(cars)

#  filter the data
print("filter the data")
heavy_engines = cars[cars['cyl'] > 6]
print(heavy_engines)

#  fillet both cols like two
filtered_new = (cars["cyl"] > 6) & (cars["hp"] > 200)
filtered_review = cars[filtered_new]
print(filtered_review)




#  Visualizing the Data Set 
