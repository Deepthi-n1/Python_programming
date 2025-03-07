import numpy as np
from scipy import stats

data = [2, 4, 6, 8, 10]

mean = np.mean(data)
print(mean)  # Output: 6.0

median = np.median(data)
print(median)  # Output: 6.0

mode_result = stats.mode(data)
mode = mode_result.mode[0]
print(mode)  # Output: 2
