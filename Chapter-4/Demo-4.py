# Access a value from a pandas Series with labels:

import pandas as pd

# Data

data = [10, 20, 30, 40, 50]

s = pd.Series(data, index=["value_1", "value_2", "value_3", "value_4", "value_5"])

#now we can use new indexes
print(s["value_3"])

