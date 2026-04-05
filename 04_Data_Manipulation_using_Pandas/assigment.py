
# Problem Statement:

# You work in XYZ Corporation as a Data Analyst. Your corporation has told you to
# analyze the customer_churn dataset with various functions.

# Tasks To Be Performed:
# 1. Start off by importing the customer_churn.csv file in the jupyter notebook
# and store that in churn DataFrame.
# 2. From the churn DataFrame, select only 3rd, 7th, 9th, and 20th columns
# and all the rows and store that in a new DataFrame named newCols.
# 3. From the original DataFrame, select only the rows from the 200th index till
# the 1000th index(inclusive) column.
# 4. Now select the rows from 20th index till 200th index(exclusive),and
# columns from 2nd index till 15th index value.
# 5. Display the top 100 records from the original DataFrame.
# 6. Display the last 10 records from the DataFrame.
# 7. Display the last record from the DataFrame.
# 8. Now from the churn DataFrame, try to sort the data by the tenure column
# according to the descending order.
# 9. Fetch all the records that are satisfying the following condition:
# a. Tenure>50 and the gender as ‘Female’
# b. Gender as ‘Male’ and SeniorCitizen as 0
# c. TechSupport as ‘Yes’ and Churn as ‘No’
# d. Contract type as ‘Month-to-month’ and Churn as ‘Yes’
# 10. Use a for loop to calculate the number of customers that are getting the


import pandas as pd
# Load the dataset into the 'churn' DataFrame
# churn = pd.read_csv("customer_churn.csv")
churn = pd.read_excel("somecars1.xlsx")

# Quick check to see if the data loaded correctly
churn.head()
print(f"Total Customers: {churn.shape[0]}")
print(f"Total Features: {churn.shape[1]}")


newcolumn =churn.iloc[:,[2, 6, 8]]
print(newcolumn.head())


# .iloc[row_start : row_stop_exclusive, column_start : column_stop]
newrows = churn.iloc[1:10, :]

# Verify the result
print(f"First index: {newrows.index[0]}")
print(f"Last index: {newrows.index[-1]}")
print(f"Total rows: {newrows}")
print(f"Total rows: {len(newrows)}")



new_slice = churn.iloc[2:14, 2:]

# Verify the dimensions of your new subset
print(f"Rows selected: {new_slice.shape[0]}")
print(f"Columns selected: {new_slice.shape[1]}")
print(new_slice.head())



print(churn.head(10))
print(churn.tail(10))
print(churn.tail(1))


churn_sorted = churn.sort_values(by='disp', ascending=False)
print(churn_sorted.head())
print("------------------------------------------------------------")
filter_a = churn[(churn['drat'] >3) & (churn['carb'] == 1)]
print(filter_a.head())


filter_b = churn[(churn['mpg'] == 160.0) & (churn['qsec'] == 1)]
print(filter_b.head())


count = 0
for index, row in churn.iterrows():
    if (row['disp'] > 100) and (row['qsec'] > 1) and (row['vs'] == 1):
        count += 1

print(f"Total Male Senior Citizens with Tech Support: {count}")



