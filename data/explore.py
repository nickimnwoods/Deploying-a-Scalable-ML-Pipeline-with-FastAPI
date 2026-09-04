import pandas as pd

df = pd.read_csv('data/census.csv')
print(df.shape) #look at number of rows and columns of dataset
print(df.columns.tolist()) #show list of column names
print(df.head()) #show top 5 rows of data
print(df.dtypes) #show datatypes of columns
print(repr(df['workclass'].unique()[:3])) #check for leading or trailing white space
print((df== ' ?').sum())  #check for placeholder values
print(df.isna().sum())  #check for missing values