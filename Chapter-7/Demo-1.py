# Create Categorical Series in Pandas

import pandas as pd

# Create a Categorical Series
s = pd.Series(['p', 'q', 'r', 's', 'q'], dtype="category")

# Display the Series
print(s)

# Apeend a Category
s = s.cat.add_categories("t")

# Display the Updated Category
print(s)
