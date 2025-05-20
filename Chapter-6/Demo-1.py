# Combine two pandas Series

import pandas as pd

#Data
data1 = [10, 20, 30, 40, 50]
data2 = [60, 70, 80]


#Create Series using Series() method

series1 = pd.Series(data1)
series2 = pd.Series(data2)

def demo(x1, x2):
    if(x1 > x2):
        return x1
    else:
        return x2

# Combine two string into one
# The function return large value

res = series1.combine(series2, demo)
print(res)