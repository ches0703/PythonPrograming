# Example of class Date
class Date:
    def __init__(self, yr, mn, dy):
        self.setYear(yr)
        self.setMonth(mn)
        self.dy = dy

    # def __lt__(self, other):
    # 직접 구현

    # def __str__(self):
    # 직접 구현

# Accessor --------------------------------------
    def getYear(self):
        return self.yr

    def getMonth(self):
        return self.mn

    def getDay(self):
        return self.dy

# Mutator ---------------------------------------
    def setYear(self, yr):
        if isinstance(yr, int):  # Type Check
            if 0 < yr:
                self.yr = yr
                return
            else:  # If enterd year < 0
                print("Error : Enterd Year is less than 0. in setYear()")
        else:  # Type Error
            print("Error : entered wrong type value Year. in setYear()")
        # Setting defaulte
        print("Setting defaulte...")
        self.yr = 1

    def setMonth(self, mn):
        if isinstance(mn, int):  # Type Check
            if 0 < mn < 13:
                self.mn = mn
                return
            else:  # If enterd year < 0
                print("Error : Enterd Month is out of range. in setYear()")
        else:  # Type Error
            print("Error : entered wrong type value Month. in setMonth()")
        # Setting defaulte
        print("Setting defaulte...")
        self.mn = 1

    def setDay(self, dy):
        if isinstance(dy, int):  # Type Check
            if self.mn in [1, 3, 5, 7, 8, 10, 12]:
                if 0 < dy < 32:
                    self.dy = dy
                    return
                else:
                    print("Error : Enterd Day is out of range. in setDay()")

        else:  # Type Error
            print("Error : entered wrong type value Day. in getDay()")
        # Setting defaulte
        print("Setting defaulte...")
    # 설정 값의 검사 기능 포함, 직접 구현

    def isLeapYear(self, yr):
        if (self.yr % 400 == 0) or ((self.yr % 4 == 0) and (self.yr % 100 != 0)):
            return True
        else:
            return False


######################################################
# Application
#‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐

if __name__ == "__main__":
    dates = [
        Date(2000, 9, 15),
        Date(1997, 2, 20),
        Date(2001, 5, 2),
        Date(2001, 5, 1),
        Date(1999, 3, 1)
    ]
    print("dates before sorting : ")
    for d in dates:
        print(d)
    #
    dates.sort()
    print("\nstudents after sorting : ")
    for d in dates:
        print(d)
