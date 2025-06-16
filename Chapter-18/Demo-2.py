# Upper() method in pandas 

# import pandas
import pandas as pd 

# Create Data
data = ["Laksh", "Harsh", "Taksh", "Daksh", "Sahil"]

# Convert list to Series
series = pd.Series(data)

# Print Series in Upper case
print(series.str.upper())
