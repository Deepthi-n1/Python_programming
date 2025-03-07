import pandas as pd
import numpy as np

# Create a Series from a list
data = [1, 3, 5, np.nan, 6]
s = pd.Series(data)
print(s)

# Uncomment the line below to debug the type of the first element in the list
#print(type(data[0]))
