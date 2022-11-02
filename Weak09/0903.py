import shutil
import os
import os.path
import zipfile


PyTempDir = "Weak09/PyTempDir"
file_1 = "Weak09/PyTempDir/file_1.txt"
file_2 = "Weak09/PyTempDir/file_2.txt"

if not (os.path.exists(PyTempDir)):
    print("Directory {} is not existing... Create new Directory...".format(PyTempDir))
    os.mkdir(PyTempDir)

if not (os.path.exists(file_1)):
    with open(file_1, "w") as f1:
        f1.write("Test File 1.")


if not (os.path.exists(file_2)):
    print("\nCopy from {} to {}".format(file_1, file_2))
    shutil.copy(file_1, file_2)

print("\nFiles in {} : ".format(PyTempDir))
for dirName, subDirList, Fnames in os.walk(PyTempDir):
    for Fname in Fnames:
        print(os.path.join(dirName, Fname))
print()

zf_name = "Weak09/PyTempDir/Py_zip.zip"
zf = zipfile.ZipFile(zf_name, mode="w", compression=zipfile.ZIP_DEFLATED)
zf.write(file_1)
zf.write(file_2)
zf.close()

zf = zipfile.ZipFile(zf_name, mode="r")
files = zf.namelist()
for file in files:
    print("file in zf : ", file)
zf.close()

print("\nDelete both test files and Directory")
os.remove(file_1)
os.remove(file_2)
os.remove(zf_name)
os.rmdir(PyTempDir)
