import numpy as np
import pandas as pd

data = {'A': [1, 2, np.nan, 4],
'B': [5, np.nan, 7, 8],
'C': [9, 10, 11, np.nan]}
df = pd.DataFrame(data)
print(df)
# Drop rows with missing values
df.dropna(inplace=True) # Modify df directly
print(df) # Print the modified DataFrame

# Fill missing values with 0
df.fillna(0, inplace=True)
print(df)
# Fill missing values with the mean of the column
df["C"].fillna(df["C"].mean(), inplace=True)
print(df)
#if you are getting errors, then copy df to another dataframe
