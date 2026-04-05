#series obj in pandas

import pandas as pd

data = [1,2,3,4]
series1 = pd.Series(data)
print(series1)

# type

print(type(series1))

# change the index name
series1.index = ["a","b","c","d"]
print(series1)

# data frame
data = [1,2,3,4,5,6,7,8]
df = pd.DataFrame(data)
print(df)
df = pd.Series(data)
df.inedx = ["a","b","c","d","e","f","g","h"]
print(df)


# using disct


dic = {
    "fruite":["Apple", "Mango", "Banana", "Orange"],
    "count":[30,40,50,60]
}

df = pd.DataFrame(dic)
print(df)


# creating a dataframe using a series 

seriesOne = pd.Series([6,12], index = ['a','b'])
df = pd.DataFrame(seriesOne)
print(df)

import numpy as np
numpyarray = np.array([[5000,6000],["Ramesh","Rajesh"]])
df = pd.DataFrame({"name":numpyarray[1], "salary":numpyarray[0]})
print(df)

# merge operarion b/w to operation

cropeItems = ["wheet","maize","Coners"]
cost = [ 2200, 3300, 4400]
quality = ["hybrid","Original","mixed"]
df1 = pd.DataFrame({
    "cropeItems":cropeItems,
    "cost":cost,
    "quality" :quality
})
print(df1)


cropeItems = ["wheet","Apple","gova"]
date = [ 280, 330, 400]
quality = ["hybrid","Original","mixed"]
df2 = pd.DataFrame({
    "cropeItems":cropeItems,
    "date":date,
    "quality" :quality
})
print(df2)
print("----------------------------------------------------------------")
print(df1.merge(df2, on="quality", how="inner"))
print("----------------------------------------------------------------")
print(df1.merge(df2, on="cropeItems", how="left"))
print("----------------------------------------------------------------")
print(df1.merge(df2, on="cropeItems", how="right"))
print("----------------------------------------------------------------")
print(df1.merge(df2, on="cropeItems", how="outer"))



#  join operate 
cropeItems = ["wheet","Apple","gova"]
date = [ 280, 330, 400]
quality = ["hybrid","Original","mixed"]
df5 = pd.DataFrame({
    "cropeItems":cropeItems,
    "date":date,
    "quality" :quality
},index = ['L1','L2',"L3"])

print(df5)






cropeItems = ["wheet","Apple","gova"]
date = [ 280, 330, 400]
quality = ["hybrid","Original","mixed"]
df6 = pd.DataFrame({
    "cropeItems":cropeItems,
    "date":date,
    "quality" :quality
},index = ['L2',"L3",'L4'])

print(df6)


# Use lsuffix (left) and rsuffix (right) to handle overlapping names
result = df5.join(df6, how="inner", lsuffix='_left', rsuffix='_right')
print(result)


# Use lsuffix (left) and rsuffix (right) to handle overlapping names
result = df5.join(df6, how="left", lsuffix='_left', rsuffix='_right')
print(result)

# Use lsuffix (left) and rsuffix (right) to handle overlapping names
result = df5.join(df6, how="right", lsuffix='_left', rsuffix='_right')
print(result)


# Use lsuffix (left) and rsuffix (right) to handle overlapping names
result = df5.join(df6, how="outer", lsuffix='_left', rsuffix='_right')
print(result)


# Use lsuffix (left) and rsuffix (right) to handle overlapping names
result = pd.concat([df5,df6])
print(result)

