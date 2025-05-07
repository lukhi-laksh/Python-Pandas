# Concatenate two pandas DataFrame

import pandas as pd

#dataset
data1 = {
    'id': ["S01", "S02", "S03", "S04", "S05"],
    'Student': ["Laksh", "Taksh", "Daksh", "Taksh", "Darsh"],
    'Roll': [101, 102, 103, 104, 105],
}

data2 = {
    'id': ["S06", "S07", "S08", "S09", "S10"],
    'Student': ["Paresh", "Jayesh", "Suresh", "Rajesh", "Naresh"],
    'Roll': [106, 107, 108, 109, 110],
}

# DataFrame
dataFrame1 = pd.DataFrame(data1, index=["Student_1", "Student_2", "Student_3", "Student_4", "Student_5",])
dataFrame2 = pd.DataFrame(data2, index=[ "Student_6", "Student_7", "Student_8", "Student_9", "Student_10",])

# Concatenate Two dataframe

resDf = pd.concat([dataFrame1, dataFrame2])
print(resDf)
