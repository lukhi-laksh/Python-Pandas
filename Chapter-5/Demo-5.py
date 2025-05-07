# check NaN in Series
import pandas as pd

# Data

data = [10, 20, 30, 40, 50]

s = pd.Series(data)

print(s.hasnans)