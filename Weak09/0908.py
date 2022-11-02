import pandas as pd

st_ids = [1201, 2202, 1203, 1701, 1500]
st_data = {
    "st_name": ["kim", "Lee", "Park", "Yoon", "Choi"],
    "Eng": [95.7, 92.4, 85.7, 76.8, 98.9],
    "Kor": [92.3, 94.5, 88.7, 80.2, 97.2],
    "Math": [95.2, 93.5, 90.3, 83.5, 98.2]
}

df = pd.DataFrame(st_data, index=st_ids)
print("df = \n", df)
print()

sci_data = [75.9, 92.4, 87.3, 75.4, 95.3]
# df.loc[:, "Sci"] = sci_data
df["Sci"] = sci_data
print("After df.loc[:,\"Sci\"] = sci_data")
print(df)
print()

avgs_per_st = df.mean(1)
df.loc[:, "Avg"] = avgs_per_st
print("After df.loc[:,\"Avg\"] = sci_data")
print(df)
print()

avgs_per_class = df.mean()
df.loc[len(df)] = avgs_per_class
df.at[len(df) - 1, "st_name"] = "Total_Avg"
print("After append Total Avg")
print(df)
print()
