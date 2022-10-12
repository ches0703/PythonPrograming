import sys
import os
import array

print(sys.platform)

print(os.getcwd)

print(os.listdir())

os.system("ipconfig")

dir = "C:/Users/ches0/Desktop/DataStructure/DataStructure"

print(os.path.exists(dir))


A = array.array('i')
print(type(A))
A.append(1)
print(A)
print(A.pop())
print(A)