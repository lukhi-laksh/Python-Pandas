# Sorting in Pandas. We can use by 

import pandas as pd

data = {
    'Id': [101, 102, 103, 104, 105],
    'Student': ["Amit", "John", "Laksh", "Taksh", "Darsh"],
    'Roll': [5, 4, 3, 2, 1],
    'Rank': [1, 2, 3, 4, 5], 
    'Marks': [90, 85, 80, 75, 40],
    'Address': ["East", "West", "North", "South", "NorthEast"]

}

# Convert data to dataframe
df = pd.DataFrame(data, index=["RowA", "RowB", "RowC", "RowD", "RowE"])

# Print dataFrame
print(df)

# Dataframe sort by Roll No
print(df.sort_values(by=["Roll"]))
