# Pandas dropna() Method

import pandas as pd 

df = pd.read_excel("C:\\Users\\luxlu\\Desktop\\Book1.xlsx")

print(df)

resDF = df.dropna()
print(resDF)