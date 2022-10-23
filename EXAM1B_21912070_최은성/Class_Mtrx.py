# User-defined Module – Class_Mtrx.py
# 21912070 최은성
class Mtrx:
    "Class of Mtrx : name, n_row, n_col, L_data"
# Init ------------------------------------------

    def __init__(self, name, n_row, n_col, L_data):
        self.set_name(name)
        self.n_row = n_row
        self.n_col = n_col
        self.L_data = L_data
        self.matrix = [[0 for j in range(n_col)] for i in range(n_row)]
        for i in range(n_row):
            self.matrix[i] = L_data[i * n_col: (i + 1) * n_col]

# Mutator ---------------------------------------
    def set_name(self, name):
        if isinstance(name, str):  # Type check
            self.name = name
            return
        else:
            print("Error : Enterd value is Not accepted Type. in setName()")
            # Setting defaulte
            print("Setting defaulte...")
            self.name = "None"

# Method ----------------------------------------
    # toString
    def __str__(self):
        S = ""
        S += self.name + " = \n"
        for i in self.matrix:
            for j in i:
                S += "{:5.2f} ".format(j)
            S += "\n"
        return S

    # "+" Operator
    def __add__(self, other):
        if (self.n_row == other.n_row) and\
                (self.n_col == other.n_col):  # Check Matrix add condition
            resulte = Mtrx("Temp", self.n_row, self.n_col, self.L_data)
            temp_L_data = []
            for i in range(self.n_row):
                for j in range(self.n_col):
                    resulte.matrix[i][j] += other.matrix[i][j]
                    temp_L_data.append(resulte.matrix[i][j])
            resulte.L_data = temp_L_data
            return resulte
        else:  # condition not satisfied
            print("Error : Matrix sum condition not satisfied")
            # return blank List
            return []

    # "-" Operator
    def __sub__(self, other):
        if (self.n_row == other.n_row) and\
                (self.n_col == other.n_col):  # Check Matrix sub condition
            resulte = Mtrx("Temp", self.n_row, self.n_col, self.L_data)
            temp_L_data = []
            for i in range(self.n_row):
                for j in range(self.n_col):
                    resulte.matrix[i][j] -= other.matrix[i][j]
                    temp_L_data.append(resulte.matrix[i][j])
            resulte.L_data = temp_L_data
            return resulte
        else:  # condition not satisfied
            print("Error : Matrix sub condition not satisfied")
            # return blank List
            return []

    # "*" Operator
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
            resulte = Mtrx("Temp", self.n_row, other.n_col, resulte_list)
            return resulte
        else:  # condition not satisfied
            print("Error : Matrix mul condition not satisfied")
            # return blank List
            return []

    def transpose(self):  # returns transposed matrix
        # Make new Mtrix
        temp = Mtrx("Temp", self.n_col, self.n_row, self.L_data)
        # Transform
        for i in range(self.n_row):
            for j in range(self.n_col):
                temp.matrix[j][i] = self.matrix[i][j]
        return temp

