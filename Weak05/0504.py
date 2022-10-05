double = lambda x : x*x


x = 25
hex_str = hex(x)
print(hex_str)
x_int = int(hex_str, 16)
print(x_int)
print("format : {:#0x}".format(x_int))

print("abs(-19) = ", abs(-19))
print("div(7/3) : ", divmod(7, 3))
print("pow(2,10) : ", pow(2, 10))
print("2 ** 10 = ", 2 ** 10)

print("double : ", double)
print("double : ", double(3))
