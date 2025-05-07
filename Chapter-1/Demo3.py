# Access group of rows or columns in pandas DataFrame.

import pandas as pd

#Dataset

data = {
    'Student': ["Laksh", "Amit", "John", "Jakob", "Devid", "Steve"],
    'Rank': [1, 2, 3, 4, 5, 6],
    'Marks': [99, 98, 97, 96, 95, 94],
}

df = pd.DataFrame(data, index=["RowA", "RowB", "RowC", "RowD", "RowE", "RowF"])

print(df)

print("\n Value = ", df.loc["RowC", "Marks"])
print(df.loc["RowD", "Marks"])