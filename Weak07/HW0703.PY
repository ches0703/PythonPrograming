# HW0703.py
"""
Project : Example of class inheritance in Python
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 17
Update list:
    - v1.1 : 10 / 17
        Make Date Class :
            Part : Init, Operator, Method, Accessor, Mutator
            Add Main area (Application)
            Add Test Time value in times: Time(25, 60, 100)
            Fix Error Message of out of value, print Enterd value
"""


class Time:
    "Class of Time : hr, mn, sec"
# Init ------------------------------------------

    def __init__(self, hr, mn, sec):
        self.setHour(hr)
        self.setMinute(mn)
        self.setSecond(sec)

# Method ----------------------------------------
    def __lt__(self, other):
        # self.hr < other.hr
        if self.getHour() < other.getHour():
            return True
        # self.hr == other.hr
        # self.mn < other.mn
        elif (self.getHour() == other.getHour()) and\
             (self.getMinute() < other.getMinute()):
            return True
        # self.yr == other.yr
        # self.mn == other.mn
        # self.dy < other.dy
        elif (self.getHour() == other.getHour()) and\
             (self.getMinute() == other.getMinute()) and\
             (self.getSecond() < other.getSecond()):
            return True
        # self.yr >= other.yr
        else:
            return False

    def __str__(self):
        return "( {:2}, {:2}, {:2} )".\
            format(self.getHour(), self.getMinute(), self.getSecond())

# Acessor ---------------------------------------
    # Hour
    def getHour(self):
        return self.hr

    # Minute
    def getMinute(self):
        return self.mn

    # Second
    def getSecond(self):
        return self.sec

# Mutator ---------------------------------------

    # Hour
    def setHour(self, hr):
        if isinstance(hr, int):  # Type Check
            if 0 <= hr < 24:
                self.hr = hr
                return
            else:  # Enterd Hour is out of range
                print("Error : Enterd Hour is out of range. in setHour(), " +
                      "Enterd value = {}".format(hr))
        else:  # Type Error
            print("Error : entered wrong type value in Hour. in setHour()")
        # Setting defaulte
        print("Setting defaulte...")
        self.hr = 0

    # Minute
    def setMinute(self, mn):
        if isinstance(mn, int):  # Type Check
            if 0 <= mn < 60:
                self.mn = mn
                return
            else:  # Enterd Miniute is out of range
                print("Error : Enterd Minute is out of range. in setMinute(), " +
                      "Enterd value = {}".format(mn))
        else:  # Type Error
            print("Error : Entered wrong type value in Minute. in setMinute()")
        # Setting defaulte
        print("Setting defaulte...")
        self.mn = 0

    # Second
    def setSecond(self, sec):
        if isinstance(sec, int):  # Type Check
            if 0 <= sec < 60:
                self.sec = sec
                return
            else:  # Enterd Second is out of range
                print("Error : Enterd Second is out of range. in setSecond(), " +
                      "Enterd value = {}".format(sec))
        else:  # Type Error
            print("Error : Entered wrong type value in Second. in setSecond()")
        # Setting defaulte
        print("Setting defaulte...")
        self.sec = 0


######################################################
# Application
######################################################

times = [
    Time(23, 59, 59),
    Time(9, 0, 5),
    Time(13, 30, 0),
    Time(3, 59, 59),
    Time(0, 0, 0),
    Time(25, 60, 100)  # Code causing the Error
]
print("times before sorting : ")
for t in times:
    print(t)
#
times.sort()
print("\ntimes after sorting : ")
for t in times:
    print(t)
