# lower() method in pandas 

import pandas as pd 

data = ["Laksh", "Harsh", "Taksh", "Daksh", "Sahil"]

series = pd.Series(data)

print(series.str.lower())