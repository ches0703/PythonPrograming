from HW0701_Student import Student


def compareStudent(st1, st2, key):
    if key == "st_id":
        if st1.st_id < st2.st_id:
            return True
        else:
            return False
    else:
        return True
# 나머지 부분은 직접 구현할 것


def sortStudent(L_st, key):
    for i in range(0, len(L_st)):
        min_idx = i
        for j in range(i + 1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], key):
                min_idx = j
        if min_idx != i:
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]


def printStudents(L_st):
    for s in range(len(L_st)):
        print(L_st[s])


if __name__ == "__main__":
    students = [
        Student("Kim", 990101, 21, 12345, "EE", 4.0),
        Student("Lee", 980715, 22, 11234, "ME", 4.2),
        Student("Park", 101225, 20, 10234, "ICE", 4.3),
        Student("Hong", 110315, 19, 13123, "CE", 4.1),
        Student("Yoon", 971005, 23, 11321, "ICE", 4.2),
        Student("Wrong", 100000, 23, 15321, "??", 3.2)]
    print("students before sorting : ")
    printStudents(students)
    #
    sortStudent(students, "name")
    print("\nstudents after sorting by name : ")
    printStudents(students)
    #
    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudents(students)
    #
    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudents(students)
