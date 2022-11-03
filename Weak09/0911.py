import pandas as pd

file_name = "Weak09/ta_20221104014849.csv"
Temp_DG = pd.read_csv(file_name, encoding="EUC-KR")
print(Temp_DG)
print(Temp_DG.describe())

temp_H = Temp_DG["High"].max()
temp_L = Temp_DG["Low"].min()

print("Max : ", temp_H)
print("Low : ", temp_L)

HighestDay = Temp_DG[Temp_DG.High >= temp_H]
print("Highest Day :\n", HighestDay)
LowestDay = Temp_DG[Temp_DG.Low <= temp_L]
print("Lowest Day :\n", LowestDay)