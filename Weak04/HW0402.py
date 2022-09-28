students = [
    ("Kim, S.C.", 12001234, "CE", 4.10),
    ("Choi, Y.B.", 119003234, "EE", 3.78),
    ("Hong, C.H.", 21001547, "ICE", 4.13),
    ("Yoon, J.H.", 17002571, "ME", 3.55),
    ("Lee, S.H.", 20003257, "ICE", 4.45),
    ("Kim, H.Y.", 19001234, "CE", 4.17),
    ("Lee, J.K.", 18003234, "EE", 3.78),
    ("Park, S.Y.", 21001643, "ICE", 4.13),
    ("Jang, S.H.", 19002567, "ME", 3.35),
    ("Yeo, C.S.", 20005243, "CE", 4.45)
]

for i in range(len(students)):
    print("students[{:2}]".format(i), end=" : ")
    print("name(", students[i][0], end=" ), ")
    print("major({:3}, GPA({:4}))".format(students[i][2], students[i][3]))
print()

print("After sorting in increasing order :")
sorted_students = sorted(students)
for i in range(len(sorted_students)):
    print("students[{:2}]".format(i), end=" : ")
    print("name(", sorted_students[i][0], end=" ), ")
    print("major({:3}, GPA({:4}))".format(
        sorted_students[i][2], sorted_students[i][3]))
print()

print("After sorting according to GPA in decreasing order :")
sorted_gpa_students = sorted(
    students, key=lambda student: student[3], reverse=True)
for i in range(len(sorted_gpa_students)):
    print("students[{:2}]".format(i), end=" : ")
    print("name(", sorted_gpa_students[i][0], end=" ), ")
    print("major({:3}, GPA({:4}))".format(
        sorted_gpa_students[i][2], sorted_gpa_students[i][3]))
