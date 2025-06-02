# Indexing in the padnas using the indexing operator

import pandas as pd

# Import CSV
df = pd.read_excel("C:\\Users\\luxlu\Desktop\\new_datas.xlsx")

# Convert CSV file to Dataframe
rs = df["Marks"]

# Print Dataframe
print(rs)
