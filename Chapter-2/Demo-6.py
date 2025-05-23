# Pandas DataFrame T Attribute
import pandas as pd

# Dataset
data = {
    'Student': ["Amit", "John", "Jcob", "David", "Stive"],
    'Rank': [1, 5, 4, 2, 3],
    'Marks': [44, 78, 46, 34, 98],
}

# Cerate a dataframe using DataFrame()

df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])
print(df)

#Convert Column to row wise
print(df.T)
