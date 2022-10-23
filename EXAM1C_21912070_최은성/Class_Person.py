# user-defined module - Class_Person.py
# 21912070 최은성

# Person Class-----------------------------------
class Person:
    "Class of Person : name, reg_id, age"
# Init ------------------------------------------

    def __init__(self, name):
        self.setName(name)  # name

# Mutator ---------------------------------------
    # name
    def setName(self, name):
        if isinstance(name, str):  # Type Check
            self.name = name
        else:  # name != string
            print("Error : entered wrong type value for Person.setName().")
            print("Setting as default...")
            self.name = "None"

# Accessor --------------------------------------
    # Name
    def getName(self):
        return self.name

# Method ----------------------------------------
    # to String
    def __str__(self):
        return "{:6}".format(self.getName())

# End Class Person ------------------------------
