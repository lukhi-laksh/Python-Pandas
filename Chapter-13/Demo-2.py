# Drop column using drop()

# Import pandas
import pandas as pd

# Create data
data = {
    'Id': [101, 102, 103, 104, 105],
    'Student': ["Amit", "John", "Laksh", "Taksh", "Darsh"],
    'Roll': [5, 4, 3, 2, 1],
    'Rank': [1, 2, 3, 4, 5], 
    'Marks': [90, 85, 80, 75, 40],
    'Address': ["East", "West", "North", "South", "NorthEast"]

}

# Convwer Data to dataframe
df = pd.DataFrame(data)

# Print Dataframe
print(df)

resDf = df.drop(3, axis="index")
print(resDf)
