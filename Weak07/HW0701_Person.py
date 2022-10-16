# HW0701_Person.py
"""
Project : Example of class Person, class Student inheritance in Python
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 17
Update list:
    - v1.1 : 10 / 17
        Make Class Person :
            Part : Init, Mutator, Accessor, Method
    - v1.2 : 10 / 17
        Devide Person Class from HW0701_Main       
        Make Testing Area to test
"""


# Person Class-----------------------------------
class Person:
    "Class of Person : name, reg_id, age"
# Init ------------------------------------------

    def __init__(self, name, reg_id, age):
        self.setName(name)
        self.setRegId(reg_id)
        self.setAge(age)

# Mutator ---------------------------------------
    # name
    def setName(self, name):
        if isinstance(name, str):
            self.name = name
        else:  # name != string
            print("Error : entered wrong type value for Person.setName().")
            print("Setting as default...")
            self.name = "None"

    # reg_id
    def setRegId(self, reg_id):
        if isinstance(reg_id, int):
            if 0 < reg_id:
                self.reg_id = reg_id
                return
            else:  # If the entered reg_id is a negative integer
                print("Error : entered value is out of range for Person.setRegId().")
        else:  # reg_id != int
            print("Error : entered wrong type value for Person.setRegId().")
        # Setting as default
        print("Setting as default...")
        self.reg_id = 0

    # age
    def setAge(self, age):
        if isinstance(age, int):
            if 0 <= age:
                self.age = age
                return
            else:  # If the entered age is a negative integer
                print("Error : entered value is out of range for Person.setAge().")
        else:  # age != int
            print("Error : entered wrong type value for Person.setAge().")
        # Setting as default
        print("Setting as default...")
        self.age = 0

# Accessor --------------------------------------
    def getName(self):
        return self.name

    def getRegId(self):
        return self.reg_id

    def getAge(self):
        return self.age

# Method ----------------------------------------
    def __str__(self):
        return "{:6}, {:8}, {:3}"\
            .format(self.getName(), self.getRegId(), self.getAge())

# End Class Person ------------------------------


# Testing Area
if __name__ == "__main__":
    P = Person("Kim", 990101, 21)
    print(P) 