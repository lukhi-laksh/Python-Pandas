# Pandas notnull() Method

import pandas as pd

# Convert Excel file to Dataframe
df = pd.read_excel("C:\\Users\\luxlu\\Desktop\\Book1.xlsx")

print(df)

# Replace null with NaN
resDF = df.notnull()
print(resDF)

