import shutil
import os
import os.path

PyTempDir = "Weak09/PyTempDir"
file_1 = "Weak09/PyTempDir/file_1.txt"
file_2 = "Weak09/PyTempDir/file_2.txt"

if not (os.path.exists(PyTempDir)):
    print("Directory {} is not existing... Create new Directory...".format(PyTempDir))
    os.mkdir(PyTempDir)

if os.path.exists(file_1):
    print("File already exists... Remove the File")
    os.remove(file_1)
else:
    print("{} is not existing... Create new File".format(file_1))

with open(file_1, "w") as f1:
    f1.write("Test File 1.")

file_size = os.path.getsize(file_1)
print("{} size : {}".format(file_1, file_size))

shutil.copy(file_1, file_2)
file_size = os.path.getsize(file_2)
print("{} size : {}".format(file_2, file_size))

print("\nFiles in {} : ".format(PyTempDir))
for dirName, subDirList, Fnames in os.walk(PyTempDir):
    for Fname in Fnames:
        print(os.path.join(dirName, Fname))

print("\nDelete both test files and Directory")
os.remove(file_1)
os.remove(file_2)
os.rmdir(PyTempDir)
