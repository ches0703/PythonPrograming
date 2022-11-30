# Fibo - Generator

def genFibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


i = 0
for f in genFibo():
    print("{}'s fibo = {}".format(i, f))
    i += 1
    if i > 20:
        break