# count() method in pandas 

import pandas as pd 

data = ["Laksh", "Harsh", "Taksh", "Daksh", "Sahil"]

# Convert list into Series
series = pd.Series(data)

# Get the length of each eliments
print(series.count())