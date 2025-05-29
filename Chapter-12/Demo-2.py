# Crate a new column at the end in Pandas Dataframe using the assign method

import pandas as pd

data = {
    'Id': [101, 102, 103, 104, 105],
    'Student': ["Amit", "John", "Laksh", "Taksh", "Darsh"],
    'Roll': [5, 4, 3, 2, 1],
    'Rank': [1, 2, 3, 4, 5], 
    'Marks': [90, 85, 80, 75, 40],
    'Address': ["East", "West", "North", "South", "NorthEast"]

}

df = pd.DataFrame(data)
print(df)

check = df.assign(check = [1, 2, 3, 3, 4])

print(check)