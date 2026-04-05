import pandas as pd
housing = pd.read_csv("housing.csv")

# 1. 
print(housing['waterfront'].value_counts())

# 2.
max_price_index = housing['price'].idxmax()
costliest_zip = housing.loc[max_price_index, 'zipcode']
print(costliest_zip)

# 3
house_garde = housing["grade"].value_counts()
print(f"Number of houses with grade 10:,{house_garde[10]}")

# 4
print(housing.isnull().sum())
print(f"Total null values: {housing.isnull().sum().sum()}")

# 5
customer_record = housing[housing['id'] == 9126100861]
print(customer_record[['id', 'waterfront']])

# 6
housing = housing['view'].value_counts()
print(f"Number of houses with 3 views: {housing[3]}")


# 8
cheapes_index = housing["price"].idxmin()
cheapes_zipcode = housing.loc[cheapes_index,"zipcode"]
print(f"The cheapest house is in zip code: {cheapes_zipcode}")

# 9
max_sqft_index = housing['sqft_living'].idxmax()
biggest_home_zip = housing.loc[max_sqft_index, 'zipcode']
print(biggest_home_zip)



# 10
max_sqft_index = housing['price'].idxmax()
costliest_year = housing.loc[max_sqft_index, 'yr_built']
print(costliest_year)


# 11
# all

# 12
# Series data type

# 13
# Index

# 14
# All of the above



# 15
# Columns

# 16
# None of the above

# 17
duplicate_rows = housing[housing.duplicated(subset=['id', 'zipcode', 'grade'])]
print(duplicate_rows)

duplicate_count = housing.duplicated(subset=['id', 'zipcode', 'grade']).sum()
print(f"Total duplicate entries found: {duplicate_count}")


# 18
# C. data.iloc[3:6,6:10]



# 19
df = pd.DataFrame({'A':[34, 78, 54], 'B':[12, 67, 43]}, index=['r1', 'r2', 'r3'])
print(df)
print(df.loc['r2':'r3'])


# 20
# D. All of the above


# 21
# A. pd.to_datetime(data['date'], format='%Y-%m-%d', utc=False, dayfirst=True)

# 22
# B. data.loc[(data["yr_built"] < 1980) & (data['floors'] > 2) & (data['bedrooms'] > 2)]


# # 23
# sample_list = [['Carl', 22],
# ['Martha', 25],
# ['Calvin', 12],
# ['Stuart', 15]
# ]
# #  c 
# print( pd.DataFrame(sample_list, columns=['Name', 'Age']))


# #   24. 
# sample_dict = {'Cristiano': ['Ronaldo','Man U', 801],
# 'Lionel': ['Messi','PSG', 758],
# 'Luis': ['Suarez','Atletico Madrid', 509],
# 'Robert': ['Lewandowski','Bayern Munich', 527],
# 'Zlatan': ['Ibrahimovic','AC Milan',553]
# }

# # B. 
# df1 = pd.DataFrame(sample_dict)
# df1 = df1.transpose()
# df1.reset_index(inplace = True)
# df1.columns = ['First Name','Last Name', 'Club', 'Goals']
# print(df1)



# #  25. 
# sample_tuple = ([1, 'one', 3],
# [2, 'two', 3],
# [3, 'Three', 5],
# [4, 'Four', 4],
# [5, 'Five', 4])
# # b
# print(pd.DataFrame(sample_tuple, columns=['Number', 'Number_text', 'txtlen']))


# 26
# b


# 27
# A. housing.describe()

# 28
# subset_rows = housing.iloc[25:36]
# print(subset_rows)

# specific_house = housing.loc[(housing['long'] == -122.045) & (housing['lat'] == 47.6168)]
# price_value = specific_house['price']
# print(price_value)

# c


# 29 B.

# 30 

# A = pd.DataFrame([['Carl', 22],['Martha', 25],['Calvin', 12],['Stuart', 15]], columns=["Name", "Age"])
# B = pd.DataFrame([['Melvin', 25],['Martha', 34],['Lewis', 32],['Leo', 25]], columns=["Name", "Age"])
# # 1. Left Outer Join
# left_join = pd.merge(A, B, on='Name', how='left')
# print(left_join)
# # 2. Outer Join
# outer_join = pd.merge(A, B, on='Name', how='outer')
# print(outer_join)
# # 3. Inner Join
# outer_join = pd.merge(A, B, on='Name', how='inner')
# print(outer_join)
# # 4. Right Outer Join
# outer_join = pd.merge(A, B, on='Name', how='right')
# print(outer_join)

# # C

# # 31 B. 0.754665.

# # 31 B. 0.754665.