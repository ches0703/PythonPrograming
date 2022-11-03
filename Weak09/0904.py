import os
import os.path
import json

ListSize = 100
L1 = list(range(ListSize))

f1 = open("Weak09/L_json.txt", "w")
json.dump(L1, f1)
f1.close()

f1_size = os.path.getsize("Weak09/L_json.txt")
print("Size of L_json : ", f1_size)
print()

f2 = open("Weak09/L_json.txt", "r")
L2 = json.load(f2)
print(L2)
f2.close()


