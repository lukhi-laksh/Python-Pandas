# Indexing in the padnas using the loc[]

import pandas as pd

# Import CSV
df = pd.read_excel("C:\\Users\\luxlu\Desktop\\new_datas.xlsx", index_col="Student")

rs = df.loc["Amit"]
print(rs)