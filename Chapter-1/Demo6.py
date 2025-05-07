# Interate Dataframe to display the columns
import pandas as pd

data = {
    'Student': ["Laksh", "Amit", "John", "Jakob", "Devid", "Steve"],
    'Rank': [1, 2, 3, 4, 5, 6],
    'Marks': [99, 98, 97, 96, 95, 94],
}

# Use the index argument to set your Index. 
df = pd.DataFrame(data, index=["Student_1", "Student_2", "Student_3", "Student_4", "Student_5", "Student_6"])
print(df)

for col in df:
    print(col)
    print(df[col].values)

