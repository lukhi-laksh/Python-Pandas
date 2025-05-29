# Crate a new column to a Pandas Dataframe using the insert() method

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

df.insert(2, "Check", ["First", "Second", "Third", "Fourth", "Fifth"])
print(df)
