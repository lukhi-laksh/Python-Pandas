# Pandas isnull() Method

import pandas as pd

# Convert Excel file to DataFrame
df = pd.read_excel("C:\\Users\\luxlu\\Desktop\\Book1.xlsx")

print(df)

resDF = df.isnull()
print(resDF)

print(df.to_string())
