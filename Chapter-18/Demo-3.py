# Title() method in pandas 

import pandas as pd 

data = ["LaKSh", "HARsh", "TakSh", "DaksH", "Sahil"]

series = pd.Series(data)

print(series.str.title())