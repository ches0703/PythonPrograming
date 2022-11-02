import pandas as pd
import numpy as np

dates = pd.date_range("20220101", periods=5)
print(dates)

temps = [[-1, 3], [-3, 2], [-5, 5], [-2, 7], [1, 10]]
df = pd.DataFrame(temps, index=dates, columns=["low", "high"])
print(df)

print("---------------------------")

df = pd.DataFrame({"Date": pd.date_range("20220101", periods=5),
                   "low": [-1, -3, -5, -2, 1],
                   "high": [3, 2, 5, 7, 10]})
print(df)
print(df.dtypes)
print("\ndf.info()")
print(df.info())

print("---------------------------")

print("df.describe()")
print(df.describe())

print("---------------------------")

print("df.T")
print(df.T)