class Point:
    def __new__(cls, *args, **kwards):
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "P = (" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, other):
        resulte = Point(x=self.x + other.x, y=self.x + self.y)
        return resulte

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False


if __name__ == "__main__":
    P1 = Point(x=1, y=3)
    print("P1 : ", P1)
    P2 = Point(x=1, y=2)
    print("P2 : ", P2)
    P3 = P1 + P2
    print("P3 = P1 + P2 : ", P3)
    P1 += P3
    print("P1 += P3 : ", P1)
    print("P1 == P2 : ", P1 == P2)
    P2 = Point(x=3, y=7)
    print("P2 = Point(x = 3, y = 7), P1 == P2 : ", P1 == P2)
