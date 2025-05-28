# # Display Bottom n rows of the dataframe in Pandas

# Import pandas as Pd

import pandas as pd 
df = pd.read_excel("C:\\Users\\luxlu\Desktop\\new_datas.xlsx")

print(df.tail(4))
