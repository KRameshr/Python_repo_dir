# import pandas as pd
# import os


# current_dir = os.path.dirname(__file__)
# # file_path = os.path.join(current_dir, 'Files', 'housing.csv')
# file_path = os.path.join(current_dir, 'Files', 'patient.csv')


# # Load the data
# data = pd.read_csv(file_path)
# print(data.columns)



# print(data.head())

# print(data.shape)
# print(data.iloc[:5, : ])
# print(data.iloc[2:5, :2 ])
# print(data.iloc[2:5, 1:2 ])
# print(data.loc[:5, "LSTAT":"MEDV" ])
# print(data.isnull().sum())
# print(data.mean())

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix  # Fixed 'sklearn' and 'matrix'
import seaborn as sns

# 1. Load the data from the 'Files' subfolder
data = pd.read_csv('Files/iris.csv')

print(data.head())
print(data.shape)