import copy


class Matrix:
    def __new__(cls, *args, **kwards):
        return super().__new__(cls)

    def __init__(self, name, n_row, n_col, list_data):
        self.name = name
        self.n_row = n_row
        self.n_col = n_col
        self.setMatrix(n_row, n_col, list_data)

    def setMatrix(self, n_row, n_col, list_data):
        # self.list_data = [[0 for j in range(n_col)] for i in range(n_row)]
        # for i in range(n_row):
        #     for j in range(n_col):
        #         self.list_data[i][j] = list_data[i][j]
        self.list_data = copy.deepcopy(list_data)

    def __str__(self):
        s = ""
        print(self.name)
        for i in self.list_data:
            for j in i:
                s += "{:3d}".format(j)
            s += "\n"
        return s


if __name__ == "__main__":
    test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    M = Matrix(name="test", n_row=3, n_col=3, list_data=test_list)
    test_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(M)
