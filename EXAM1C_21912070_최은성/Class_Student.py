# user-defined module - Class_Student.py
# 21912070 최은성

from Class_Person import *

# Sutudent Class : SubClass of Person -----------


class Student(Person):
    "Class of Person : SubClass of Person, add st_id, major, gpa"
# Class Attributes ------------------------------
    S_mj = {"EE", "ICE", "ME", "CE"}  # Set of Major

# Init ------------------------------------------
    def __init__(self, name, st_id, major, gpa):
        Person.__init__(self, name)  # SuperClass init
        self.setStId(st_id)  # set ID
        self.setMajor(major)  # set Major
        self.setGpa(gpa)  # set GPA

# Mutator ---------------------------------------
    # ID
    def setStId(self, st_id):
        if isinstance(st_id, int):  # Type Check
            if 0 <= st_id:
                self.st_id = st_id
                return
            else:  # If the entered st_id is a negative integer
                print("Error : entered value is out of range for Person.setStId().")
        else:  # st_id != int
            print("Error : entered wrong type value for Person.setStId().")
        # Setting as default
        print("Setting as default...")
        self.st_id = 0

    # Major
    def setMajor(self, major):
        if major in Student.S_mj:  # Check Exist Major 
            self.major = major
            return
        else:  # If the entered value is not in S_mj
            print("Error : entered undefined value in S_mj. So can't setMajor()")
        # Setting as default
        print("Setting as default...")
        self.major = "None"

    # GPA
    def setGpa(self, gpa):
        if isinstance(gpa, (float, int)):  # Type Check
            if 0 <= gpa <= 4.5:  # Range Check
                self.gpa = gpa
                return
            else:  # If the entered gpa is out of range
                print("Error : entered value is out of range for Person.setGpa().")
        else:  # gpa != int
            print("Error : entered wrong type value for Person.setGpa().")
        # Setting as default
        print("Setting as default...")
        self.gpa = 0

# Accessor --------------------------------------

    # ID
    def getStId(self):
        return self.st_id

    # Major
    def getMajor(self):
        return self.major

    # GPA
    def getGpa(self):
        return self.gpa

# Method ----------------------------------------
    # to String
    def __str__(self):
        return "Student ( " + super().__str__() + ", {:6}, {:5}, {:2.1f} )"\
            .format(self.getStId(), self.getMajor(), self.getGpa())

# End Class Student------------------------------

# Funfion Part-----------------------------------

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
        if st1.getGpa() > st2.getGpa():  # for Descending
            return True
        else:
            return False
    else:  # defaulte
        print("Error : as compareStudent(), entered undefined value in key.")
        # Setting as default
        print("defalte Return value : True")
        return True

# Sorting Student as Key : Selection Sort


def sortStudents(L_st, key):
    for i in range(0, len(L_st)):
        min_idx = i  # Save min index
        for j in range(i + 1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], key):
                min_idx = j
        if min_idx != i:
            # Swap : Saved min index value, real min value(i started)
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]


# Print Student info
def printStudents(L_st):
    for s in range(len(L_st)):
        print(L_st[s])



