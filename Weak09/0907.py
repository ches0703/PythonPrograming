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
print("After sort_index() :")
print(df.sort_index(axis=0))

print()
print("After sort_values(by=\"Eng\", ascending=False) :")
print(df.sort_values(by="Eng", ascending=False))

print()
print("After sort_values(by=\"Kor\", ascending=False) :")
print(df.sort_values(by="Kor", ascending=False))

print()
print("After sort_values(by=\"Math\", ascending=False) :")
print(df.sort_values(by="Math", ascending=False))


