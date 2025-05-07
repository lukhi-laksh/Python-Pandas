# Name your indexes in a Pandas Dataframe

import pandas as pd

data = {
    'Student': ["Laksh", "Amit", "John", "Jakob", "Devid", "Steve"],
    'Rank': [1, 2, 3, 4, 5, 6],
    'Marks': [99, 98, 97, 96, 95, 94],
}

# Use the index argument to set your Index. 
df = pd.DataFrame(data, index=["Student_1", "Student_2", "Student_3", "Student_4", "Student_5", "Student_6"])
print(df)

print(df.loc["Student_1", "Marks"])