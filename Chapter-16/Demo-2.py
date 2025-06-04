# Remove duplicates using the drop_duplicates()
# Handling Duplicates using duplicated()

import pandas as pd

data = {
    'Id': [101, 102, 103, 104, 105],
    'Student': ["Amit", "Harsh", "Laksh", "Taksh", "Darsh"],
    'Roll': [5, 4, 3, 2, 1],
    'Rank': [1, 2, 3, 4, 5], 
    'Marks': [90, 85, 80, 75, 40],
    'Address': ["East", "West", "North", "South", "NorthEast"]

}

# Convert data to dataframe
df = pd.DataFrame(data)

res = df.drop_duplicates('Student')
print(res)
