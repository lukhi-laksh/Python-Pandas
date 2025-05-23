# Join DataFrame in pandas

import pandas as pd

#dataset
data1 = {
    'id': ["S01", "S02", "S03", "S04", "S05"],
    'Student': ["Laksh", "Taksh", "Daksh", "Taksh", "Darsh"],
    'Roll': [101, 102, 103, 104, 105],
}

data2 = {
    'Rank': [3, 2, 4, 5, 1],
    'Marks': [12, 35, 53, 45, 23]
}

# DataFrame
dataFrame1 = pd.DataFrame(data1)
dataFrame2 = pd.DataFrame(data2)

# Join Two Dataframe

resDf = dataFrame1.join(dataFrame2)
print(resDf)

# Convert data vertical to horizantal wise print
print(resDf.T)
