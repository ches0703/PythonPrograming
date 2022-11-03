
f1 = open(".\Weak09\data.txt", "w")
f1.write("Lee 80 90 95\n")
f1.write("kim 85 50 50\n")
f1.write("Park 100 80 95\n")
f1.flush()
f1.close()

f2 = open(".\Weak09\data.txt", "r")
while True:
    read_data = f2.read()
    if read_data == "":
        break
    print(read_data)

print("f2.tell() : ", f2.tell())
f2.seek(0)
print("after f2.seek(0), f2.tell() : ", f2.tell())

list_name = []
list_s1 = []
list_s2 = []
list_s3 = []

for line in f2.readlines():
    name, s1, s2, s3 = line.split()
    list_name.append(name)
    list_s1.append(s1)
    list_s2.append(s2)
    list_s3.append(s3)

f2.close()

print("lsit_name : ", list_name)
print("list_s1 : ", list_s1)
print("list_s2 : ", list_s2)
print("list_s3 : ", list_s3)
list_student = list(zip(list_name, list_s1, list_s2, list_s3))
for i in list_student:
    print(i)