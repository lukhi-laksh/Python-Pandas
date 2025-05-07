# Crate a pandas datagram
import pandas as pd

#Dataset

data = {
    'Student': ["Laksh", "Amit", "John", "Jakob", "Devid", "Steve"],
    'Rank': [1, 2, 3, 4, 5, 6],
    'Marks': [99, 98, 97, 96, 95, 94],
}

df = pd.DataFrame(data)
print("Student record is: \n \n", df)