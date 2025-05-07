# Create a Pandas series
from operator import index

import pandas as pd

# Data

data = [10, 20, 30, 40, 50]

# Create a Series using the Series() method

s = pd.Series(data)
print(s)