class Date:

    def __init__(self, date):
        self.setDate(date)

    def setDate(self, date):
        if 1 < date < 31:
            self.date = date
        else:
            print("Error : date value is wrong!")
            self.date = -1
    
    def getData(self):
        return self.date
    
    def __str__(self):
        return "date = " + str(self.getData())


d1 = Date(3)
print(d1.date)
d2 = Date(40)
print(d2.date)
print(d1)