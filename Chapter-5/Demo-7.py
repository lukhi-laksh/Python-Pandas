# Select Upper side specific Row
import pandas as pd

# Data

data = [10, 20, 30, 40, 50]

s = pd.Series(data)

#print 2 data from uppder side
print(s.head(2))
