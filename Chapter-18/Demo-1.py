# lower() method in pandas 

import pandas as pd 

data = ["Laksh", "Harsh", "Taksh", "Daksh", "Sahil"]

# convert list into series
series = pd.Series(data)

# Print sereies in lower case
print(series.str.lower())
