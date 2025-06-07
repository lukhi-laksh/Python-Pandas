# len() method in pandas 

import pandas as pd 

data = ["Laksh", "Harsh", "Taksh", "Daksh", "Sahil"]

# Convert list into Series
series = pd.Series(data)

# Convert Text data to cemal case
print(series.str.len() )
