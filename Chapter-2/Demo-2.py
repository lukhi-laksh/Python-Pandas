# Pandas DataFrame ndim Attribute

import pandas as pd

# DataSet

data = {
    'Student': ["Amit", "John", "Jcob", "David", "Stive"],
    'Rank': [1, 5, 4, 2, 3],
    'Marks': [44, 78, 46, 34, 98],
}

# Cerate a dataframe using DataFrame()

df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])
print(df)

# Number of Dimension in the dataFrame

print(df.ndim)