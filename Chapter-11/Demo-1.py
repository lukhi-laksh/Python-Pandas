# Select More than one column

import pandas as pd 


data = {
    'Student': ["Amit", "John", "Laksh", "Taksh", "Darsh"],
    'Rank': [1, 2, 3, 4, 5], 
    'Marks': [90, 85, 80, 75, 40],
}

# Convert To dataframe
df = pd.DataFrame(data)

# Print Dataframe
print(df)
print(df[["Student", "Rank"]])
