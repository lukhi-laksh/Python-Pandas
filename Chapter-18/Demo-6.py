# contains() method in pandas 

# import pandas 
import pandas as pd 

# Create data
data = ["Laksh", "Harsh", "Taksh", "Daksh", "Sahil"]

# Convert list into pandas
series = pd.Series(data)

# Get the length of each eliments
print(series.str.contains("Laksh"))
