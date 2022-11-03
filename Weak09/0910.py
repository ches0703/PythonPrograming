import pandas as pd
# import numpy as np

st_ids = [1201, 2202, 1203, 1701, 1500]

data_1 = {"st_name": ["kim", "Lee", "Park", "Yoon", "Choi"]}

df_1 = pd.DataFrame(data_1, index=st_ids)
print("df_1\n", df_1)


data_2 = {
    "Eng": [95.7, 92.4, 85.7, 76.8, 98.9],
    "Kor": [92.3, 94.5, 88.7, 80.2, 97.2],
    "Math": [95.2, 93.5, 90.3, 83.5, 98.2],
    "Sci": [75.9, 92.4, 87.3, 75.4, 95.3]
}

df_2 = pd.DataFrame(data_2, st_ids)
print("df_2\n", df_2)

df = pd.merge(df_1, df_2, left_index=True, right_index=True, how="left")
print("df\n", df)

df = df_1.join(df_2, how="right")
print("df\n", df)

a_st_data = {"st_name": "Hwang", "Eng": 95.0, "Kor": 85.7, "Math": 97.5}
temp_df = pd.DataFrame(a_st_data, index=[3000])

df = pd.concat((df, temp_df))

print("df\n", df)

avgs_per_st = df.mean(1)
df["Avg"] = avgs_per_st

avgs_per_class = df.mean()
df.loc[len(df)] = avgs_per_class
df.loc[len(df) - 1, "st_name"] = "Total Avg"

print("df\n", df)

with pd.ExcelWriter("Weak09\Student_scores.xlsx") as excel_writer:
    df.to_excel(excel_writer, sheet_name="Student Records")
