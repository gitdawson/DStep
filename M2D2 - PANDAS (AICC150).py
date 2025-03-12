import pandas as pd
import numpy as np



# First Series works fine
Obj = pd.Series([1,2,3,4,5])

# Corrected syntax for Series with index
Obj = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])

"""""
print(Obj * 2)
print(np.exp(Obj))

sdata={"Ohio":35000,"Texas":71000}
obj3 = pd.Series(sdata)
print(obj3)
states = ["California","Ohio","Texas"]
obj4 = pd.Series(sdata, index=states)
print(obj4)
print(obj4.isna())
print(obj4.notna())
"""

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [25, 30, 35, 40],
    'City': ['', 'Los Angeles', 'Chicago', 'Houston']
             }

df = pd.DataFrame(data)

"""""
print(df)
print(df.head)
print(df.tail)
print(df.info)
print(df.describe)
print(df.shape)

print(df['Name'])
print(df[['Name', 'Age']])
print(df.iloc[1])
print(df.loc[1])
print(df.loc[1, 'Name'])
"""
print(df.isnull().sum())
df['Country'] = ['USA', 'USA', 'USA', 'USA']
print(df.sort_values(by='Age', ascending=False))
filtered_df = df[df['Age'] > 30]
print(filtered_df)
grouped = df.groupby('Age').mean() 
print(grouped)


