# HW0701_Person.py
"""
Project : Example of class Person, class Student inheritance in Python
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 17
Update list:
    - v1.1 : 10 / 17
        Devide Student Class from HW0701_Main
        Import Person Class : HW0701_Person
        Make Student Class :
            Part : Init, Mutator, Method
    - v1.2 : 10 / 17
        Make Student Class :
            Part : Accessor    
"""


from HW0701_Person import Person


# Sutudent Class : SubClass of Person -----------
class Student(Person):
    "Class of Person : SubClass of Person, add st_id, major, gpa"
# Class Attributes ------------------------------
    S_mj = {"EE", "ICE", "ME", "CE"}  # Set of Major

# Init ------------------------------------------
    def __init__(self, name, reg_id, age, st_id, major, gpa):
        Person.__init__(self, name, reg_id, age)
        self.setStId(st_id)
        self.setMajor(major)
        self.setGpa(gpa)

# Mutator ---------------------------------------
    def setStId(self, st_id):
        if isinstance(st_id, int):
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

    def setMajor(self, major):
        if major in Student.S_mj:
            self.major = major
            return
        else:  # If the entered value is not in S_mj
            print("Error : entered undefined value in S_mj. So can't setMajor()")
        # Setting as default
        print("Setting as default...")
        self.major = "None"

    def setGpa(self, gpa):
        if isinstance(gpa, (float, int)):
            if 0 <= gpa <= 4.5:
                self.gpa = gpa
                return
            else:  # If the entered gpa is a negative integer
                print("Error : entered value is out of range for Person.setGpa().")
        else:  # gpa != int
            print("Error : entered wrong type value for Person.setGpa().")
        # Setting as default
        print("Setting as default...")
        self.gpa = 0

# Accessor --------------------------------------

    def getStId(self):
        return self.st_id

    def getMajor(self):
        return self.major

    def getGpa(self):
        return self.gpa

# Method ----------------------------------------
    def __str__(self):
        return "Student ( " + super().__str__() + ", {:6}, {:5}, {:2.1f} )"\
            .format(self.getStId(), self.getMajor(), self.getGpa())

# End Class Student------------------------------
