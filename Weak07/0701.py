class Person():
    "This is testing class!"

    def __new__(cls, *args, **kwards):
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age


P = Person("Kim", 25)
print(P.name)
print(P.age)
