"""
Project : class Mtrx and Application Program
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 18
Update list:
    - v1.1 : 10 / 18
        Make Date Class :
            Part : Init, Mutator
                Method : setName(), __str__
                        __add__, __sub__, __mul
            Add Main area (Application)
"""


class Mtrx:
    "Class of Mtrx : name, n_row, n_col, L_data"
# Init ------------------------------------------
    def __init__(self, name, n_row, n_col, L_data):  # 직접 구현
        self.setName(name)
        self.n_row = n_row
        self.n_col = n_col
        self.L_data = L_data
        self.matrix = [[0 for j in range(n_col)] for i in range(n_row)]
        for i in range(n_row):
            self.matrix[i] = L_data[i * n_col: (i + 1) * n_col]

# Mutator ---------------------------------------
    def setName(self, name):
        if isinstance(name, str):  # Type check
            self.name = name
            return
        else:
            print("Error : Enterd value is Not accepted Type. in setName()")
            # Setting defaulte
            print("Setting defaulte...")
            self.name = "None"

# Method ----------------------------------------
    def __str__(self):
        S = ""
        S += self.name + " = \n"
        for i in self.matrix:
            for j in i:
                S += "{:2} ".format(j)
            S += "\n"
        return S

    def __add__(self, other):
        if (self.n_row == other.n_row) and\
                (self.n_col == other.n_col):  # Check Matrix add condition
            resulte = Mtrx("Temp", self.n_row, self.n_col, self.L_data)
            for i in range(self.n_row):
                for j in range(self.n_col):
                    resulte.matrix[i][j] += other.matrix[i][j]
            return resulte
        else:  # condition not satisfied
            print("Error : Matrix sum condition not satisfied")
            # return blank List
            return []

    def __sub__(self, other):
        if (self.n_row == other.n_row) and\
                (self.n_col == other.n_col):  # Check Matrix sub condition
            resulte = Mtrx("Temp", self.n_row, self.n_col, self.L_data)
            for i in range(self.n_row):
                for j in range(self.n_col):
                    resulte.matrix[i][j] -= other.matrix[i][j]
            return resulte
        else:  # condition not satisfied
            print("Error : Matrix sub condition not satisfied")
            # return blank List
            return []

    def __mul__(self, other):
        # Check Matrix mul condition
        if (self.n_col == other.n_row):
            resulte_list = []
            s = 0
            for i in range(self.n_row):
                for j in range(other.n_col):
                    for k in range(self.n_col):
                        s += self.matrix[i][k] * other.matrix[k][j]
                    resulte_list.append(s)
                    s = 0
            print(resulte_list)
            resulte = Mtrx("Temp", self.n_row, other.n_col, resulte_list)
            return resulte
        else:  # condition not satisfied
            print("Error : Matrix mul condition not satisfied")
            # return blank List
            return []


# Application -----------------------------------

if __name__ == "__main__":
    LA = [1, 2, 3, 4, 5,
          6, 7, 8, 9, 10,
          11, 12, 13, 14, 15]
    LB = [1, 0, 0, 0, 0,
          0, 1, 0, 0, 0,
          0, 0, 1, 0, 0]
    LC = [0, 0, 0,
          1, 0, 0,
          0, 1, 0,
          0, 0, 1,
          0, 0, 0]

    mA = Mtrx("mA", 3, 5, LA)
    print(mA)
    mB = Mtrx("mB", 3, 5, LB)
    print(mB)
    mC = Mtrx("mC", 5, 3, LC)
    print(mC)

    mD = mA + mB
    mD.setName("mD = mA + mB")
    print(mD)

    mE = mA - mB
    mE.setName("mE = mA ‐ mB")
    print(mE)

    mF = mA * mC
    mF.setName("mF = mA * mC") 
    print(mF)
