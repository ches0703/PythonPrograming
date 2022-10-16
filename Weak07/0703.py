class Person:
    def __new__(cls, *args, **kwards):
        print("P : ", args)
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name : {}, age : {}".format(self.name, self.age)


class Student(Person):
    def __new__(cls, *args, **kwards):
        print("S : ", args)
        return super().__new__(cls)

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score

    def __str__(self):
        return "name : {}, age : {}, score = {}"\
            .format(self.name, self.age, self.score)


if __name__ == "__main__":
    S = Student("kim", 22, 4.5)
    print(S)
