# Pandas fillna() Method

import pandas as pd 

df = pd.read_excel("C:\\Users\\luxlu\\Desktop\\Book1.xlsx")

print(df)

# Find and remove rows with Null values
resDF = df.fillna(111)
print(resDF)