import math
import random
print("PI = ", math.pi)

print("e = ", math.e)

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Min = ", min(L))
print("Max = ", max(L))

print("abs(-15) = ", abs(-15))
print("fabs(-0.1234) = ", math.fabs(-0.1234))

print("2^10 = ", math.pow(2, 10))
print("log10 100 = ", math.log10(100))
print("sqrt(81) = ", math.sqrt(81))

print("radom.ramdom()", random.random())
print(random.randrange(10))
print(random.randint(0, 1))
s = "abcdef"
print(random.choice(s))
print(random.sample(s, 3))
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)
