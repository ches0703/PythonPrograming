# HW0701_main.py
"""
Project : Example of class Person, class Student inheritance in Python
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 17
Update list:
    - v1.1 : 10 / 17
        Import Student Class : HW0701_Student.py
        Make compareStudent() :
            Part : name, st_id, GPA
        Add sortStudent(), printStudents(), Main area
"""
from HW0701_Student import Student


# Compare Student for Sorting
def compareStudent(st1, st2, key):
    if key == "name":  # name
        if st1.getName() < st2.getName():
            return True
        else:
            return False
    elif key == "st_id":  # st_id
        if st1.getStId() < st2.getStId():
            return True
        else:
            return False
    elif key == "GPA":  # gpa
        if st1.getGpa() < st2.getGpa():
            return True
        else:
            return False
    else:  # defaulte
        print("Error : as compareStudent(), entered undefined value in key.")
        # Setting as default
        print("defalte Return value : True")
        return True


# Sorting Student as Key : Selection Sort
def sortStudent(L_st, key):
    for i in range(0, len(L_st)):
        min_idx = i
        for j in range(i + 1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], key):
                min_idx = j
        if min_idx != i:
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]


# Print Student info
def printStudents(L_st):
    for s in range(len(L_st)):
        print(L_st[s])


# Main Area
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
    # Sorting as name
    sortStudent(students, "name")
    print("\nstudents after sorting by name : ")
    printStudents(students)
    # Sorting as st_id
    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudents(students)
    # Sorting as GPA
    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudents(students)
