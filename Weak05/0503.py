def positon_arg(x, y, z):
    print("x = {}, y = {}, z = {}".format(x, y, z))
    return x + y + z


def defalte_value(width=1, height=1):
    return width * height


def keyword_arg(x, y):
    print("{} / {} = ".format(x, y), end="")
    return x / y


def dict_arg(x, y, z):
    print("x = {}, y = {}, z = {}".format(x, y, z))
    return x + y + z


def keyword_only_func(x, *, y, z):
    print("x = {}, y = {}, z = {}".format(x, y, z))
    return x + y + z


def varposArgsFunc(*args):
    print(type(args))
    print("args :", args)


# position_arg
x = 1
y = 2
z = 3
print("position_arg(x,y,z) : x + y + z = ", positon_arg(x, y, z))

# defalte value
width = 10
height = 20
print("defalte_value(width,height) : ", defalte_value(width, height))
print("defalte_value() : ", defalte_value())

# keyword_arg
print(keyword_arg(10, 5))
print(keyword_arg(5, 10))
print(keyword_arg(y=5, x=10))

# dict_arg
print("position_arg({'x': 2, 'y': 3, 'z': 4}) : x + y + z = ",
      positon_arg(**{'x': 2, 'y': 3, 'z': 4}))

# keyword_only_func
print("keyword_only_func((1, y=5, z=10)}) : x + y + z = ",
      keyword_only_func(1, y=5, z=10))
print("keyword_only_func({1, **{'y': 3, 'z': 4}}) : x + y + z = ",
      keyword_only_func(1, **{'y': 3, 'z': 4}))

# varposArgsFunc
varposArgsFunc(1)
varposArgsFunc(1, 2)
varposArgsFunc(1, 2, 3)
