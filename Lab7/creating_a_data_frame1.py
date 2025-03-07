import pandas as pd
data_z = pd.Series([0, 1, 8, 27, 64, 125])  # Corrected Series creation
df = pd.DataFrame({"x_value": data_x, "square(x)": data_y, "cube(x)": data_z})
print(df)
print(df.values.shape, type(data.values()))
