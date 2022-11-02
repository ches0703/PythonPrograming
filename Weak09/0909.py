import pandas as pd
import numpy as np

st_data = {
    "st_id": [1201, 2202, 1203, 1701, 1500],
    "st_name": ["kim", "Lee", "Park", "Yoon", "Choi"],
    "Eng": [95.7, 92.4, 85.7, 76.8, 98.9],
    "Kor": [92.3, 94.5, 88.7, 80.2, 97.2],
    "Math": [95.2, 93.5, 90.3, 83.5, 98.2]
}

df = pd.DataFrame(st_data)
print("df :")
print(df)
print()

st_ids = df["st_id"]
print(st_ids)
print()

df["A"] = [1, np.nan, 1, 1, np.nan]
print(df)
print()

print(df.dropna(how="any"))
print()

print(df.fillna(value=0))
print()

print(df.isna())
print()

eng_scores = df["Eng"]
print(eng_scores)
print(eng_scores.min())
print(eng_scores.max())
print(eng_scores.mean())
print(eng_scores.describe())

df_part = [df[:2], df[2:]]
print(df_part[0])
print(df_part[1])
print(pd.concat(df_part))
