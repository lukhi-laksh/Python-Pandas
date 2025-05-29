# Remove a Category in Pandas

import pandas as pd

# Create data

df = pd.DataFrame({"Cat1": list("pqrs"), "Cat2": list("pqrp"), "Cat3": list("prrr")}, dtype="category")

print(df)
