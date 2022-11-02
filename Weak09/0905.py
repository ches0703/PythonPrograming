import os
import os.path

Test = b"0123456789"
print("Test : ", Test)

f_bin = open("Weak09/test.bin", "wb+")
f_bin.write(Test)
f_bin.flush()
f_bin_size = os.path.getsize("Weak09/test.bin")

for i in range(f_bin_size):
    f_bin.seek(i)
    ch = f_bin.read(1)
    print(ch)
print()
print(f_bin_size)
f_bin.close()
