# Upper() method in pandas 

import pandas as pd 

data = ["Laksh", "Harsh", "Taksh", "Daksh", "Sahil"]

series = pd.Series(data)

# Print Series in Upper case
print(series.str.upper())
