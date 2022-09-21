

a, b = input("Input two hexadecimal numbers (ex: 0xA3 0x3A) >> ").split(' ')

a = int(a, 16)
b = int(b, 16)

print("a = {0:#x} = {0:#010b}".format(a))
print("b = {0:#x} = {0:#010b}".format(b))

print("a & b = {0:#x} = {0:#010b}".format(a & b))
print("a | b = {0:#x} = {0:#010b}".format(a | b))
print("a ^ b = {0:#x} = {0:#010b}".format(a ^ b))