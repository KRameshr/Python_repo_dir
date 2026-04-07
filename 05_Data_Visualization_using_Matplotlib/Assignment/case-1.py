
# Problem Statement:
# Consider yourself to be Sam who is a data scientist. He has been approached by
# a telecom company to build some aesthetic graphs to make better sense of the
# customer data.
# Tasks To Be Performed:
# 1. Sam has to build a bar-plot for the ‘Contract’ column:
# a. Set the x-axis label to be ‘Contract Type of customer’
# b. Set the y-axis label to be ‘Count’
# c. Set the title of the plot to be ‘Distribution of Contract’
# d. Assign ‘orange’ color to all the bars
# 2. Sam has to build a histogram for the ‘MonthlyCharges’ column:
# a. Set the x-axis label to be ‘Monthly Charges Incurred’
# b. Set the y-axis label to be ‘Count’
# c. Set the title of the plot to be ‘Distribution of Monthly Charges’
# d. Assign ‘forestgreen’ color to the bins


# 3. Sam has to build a scatter-plot between ‘TotalCharges’ and ‘tenure’.
# ‘TotalCharges’ should be on the y-axis and ‘tenure’ should be on the
# x-axis.
# a. Set the x-axis label to be ‘Tenure of the customer’
# b. Set the y-axis label to be ‘Total chargesIncurred’
# c. Set the title of the plot to be ‘Total Charges vs Tenure’
# d. Assign ‘indigo’ color to the points


# 4. Sam has to build a box-plot between ‘MonthlyCharges’ and
# ‘PaymentMethod’. ‘MonthlyCharges’ should be on the y-axis and
# ‘PaymentMethod’ should be on the x-axis.
# a. Set the x-axis label to be ‘Payment Method of customer’
# b. Set the y-axis label to be ‘Monthly ChargesIncurred’
# c. Set the title of plot to be ‘Monthly Charges vs. Payment Method’
# d. Assign ‘olive’ color to the box-plots




import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('customer_churn.csv')

plt.figure(figsize=(8, 6))

contact_data = df['Contract'].value_counts()

plt.bar(contact_data.index, contact_data.values, color="orange")
plt.xlabel('Contract Type of customer')
plt.ylabel('Count')
plt.title('Distribution of Contract')

plt.show()


# histogram
plt.hist(df['MonthlyCharges'], color='forestgreen', bins=30, edgecolor='white')
plt.xlabel('Monthly Charges Incurred')
plt.ylabel('Count')
plt.title('Distribution of Contract')

plt.show()


plt.scatter(x=df['tenure'], y=df['TotalCharges'], color='indigo', alpha=0.5)
plt.xlabel('Tenure of the customer')
plt.ylabel('Total chargesIncurred')
plt.title('Total Charges vs Tenure')
plt.show()

import seaborn as sns
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['PaymentMethod'], y=df['MonthlyCharges'], color='olive')
plt.xlabel('Payment Method of customer')
plt.ylabel('Monthly ChargesIncurred')
plt.title('Monthly Charges vs. Payment Method')
plt.show()

