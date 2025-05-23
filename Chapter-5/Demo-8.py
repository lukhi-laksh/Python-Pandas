# Select bottom side specific row
import pandas as pd

# Data

data = [10, 20, 30, 40, 50]

s = pd.Series(data)

#print 2 data from bottom side
print(s.tail(2))
