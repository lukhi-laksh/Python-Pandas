# Display Bottom n rows of the dataframe in Pandas

import pandas as pd

df = pd.read_csv("C:\\Users\\luxlu\Desktop\\new_data.csv")

print(df.tail(4))