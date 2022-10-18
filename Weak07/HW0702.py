# HW0702.py
"""
Project : Example of class Date
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 17
Update list:
    - v1.1 : 10 / 17
        Make Date Class :
            Part : Init, Operator Overloading,
                   Method, Accessor, Mutator
            Add Main area (Application)
"""


class Date:
    "Class of Date : yr, mn, dy"
# Init ------------------------------------------
    def __init__(self, yr, mn, dy):
        self.setYear(yr)
        self.setMonth(mn)
        self.setDay(dy)

# Operator Overloading --------------------------
    def __lt__(self, other):  # self < other : True
        # self.yr < other.yr
        if self.getYear() < other.getYear(): 
            return True
        # self.yr == other.yr
        # self.mn < other.mn
        elif (self.getYear() == other.getYear()) and\
             (self.getMonth() < other.getMonth()):
            return True
        # self.yr == other.yr
        # self.mn == other.mn
        # self.dy < other.dy
        elif (self.getYear() == other.getYear()) and\
             (self.getMonth() == other.getMonth()) and\
             (self.getDay() < other.getDay()):
            return True
        # self.yr >= other.yr
        else:
            return False

# Method ----------------------------------------
    def isLeapYear(self, yr):
        if (yr % 400 == 0) or ((yr % 4 == 0) and (yr % 100 != 0)):
            return True
        else:
            return False

    def __str__(self):
        return "( {:4} - {:2} - {:2} )".\
            format(self.getYear(), self.getMonth(), self.getDay())

# Accessor --------------------------------------
    def getYear(self):
        return self.yr

    def getMonth(self):
        return self.mn

    def getDay(self):
        return self.dy

# Mutator ---------------------------------------
    # Year
    def setYear(self, yr):
        if isinstance(yr, int):  # Type Check
            if 0 < yr:
                self.yr = yr
                return
            else:  # If enterd year < 0
                print("Error : Enterd Year is less than 0. in setYear()")
        else:  # Type Error
            print("Error : entered wrong type value in Year. in setYear()")
        # Setting defaulte
        print("Setting defaulte...")
        self.yr = 1

    # Month
    def setMonth(self, mn):
        if isinstance(mn, int):  # Type Check
            if 0 < mn < 13:
                self.mn = mn
                return
            else:  # If enterd year < 0
                print("Error : Enterd Month is out of range. in setYear()")
        else:  # Type Error
            print("Error : entered wrong type value in Month. in setMonth()")
        # Setting defaulte
        print("Setting defaulte...")
        self.mn = 1

    # Day
    def setDay(self, dy):
        if isinstance(dy, int):  # Type Check
            # Month with 31 days
            if self.getMonth() in [1, 3, 5, 7, 8, 10, 12]:
                if 0 < dy < 32:
                    self.dy = dy
                    return
                else:
                    print("Error : Enterd Day is out of range. in setDay()")
            # Month == 2,
            elif self.getMonth() == 2:
                # Leepyear's feb has 29days
                if self.isLeapYear(self.getYear()):
                    if 0 < dy < 30:
                        self.dy = dy
                        return
                    else:
                        print("Error : Enterd Day is out of range. in setDay()")
                # else feb has 28days
                else:
                    if 0 < dy < 29:
                        self.dy = dy
                        return
                    else:
                        print("Error : Enterd Day is out of range. in setDay()")
            # Month with 30 days
            else:
                if 0 < dy < 31:
                    self.dy = dy
                    return
                else:
                    print("Error : Enterd Day is out of range. in setDay()")
        else:  # Type Error
            print("Error : entered wrong type value in Day. in setDay()")
        # Setting defaulte
        print("Setting defaulte...")
        self.dy = 1


#################################################
# Application ###################################
#################################################


if __name__ == "__main__":
    dates = [
        Date(2020, 9, 24),
        Date(2000, 9, 15),
        Date(2020, 2, 29),
        Date(2020, 1, 31),
        Date(2001, 5, 2),
        Date(2001, 5, 1),
        Date(1999, 3, 1),
        Date(2022, 10, 17),
        Date(1945, 8, 15)
    ]
    print("dates before sorting : ")
    for d in dates:
        print(d)
    #
    dates.sort()
    print("\nstudents after sorting : ")
    for d in dates:
        print(d)
