# HW31.py
"""
Project : Hexadecimal input and bit operation
Author: Eun-seong Choi
Date of last update: 2022 / 9 / 21
Update list:
    - v1,1 : 9 /21
        Make a variables and get data to stirng(a, b)
        Tranform a,b to int
        Print a,b(Hex,Bin)
        Print after operation
"""

# Get data a,b to string
a, b = input("Input two hexadecimal numbers (ex: 0xA3 0x3A) >> ").split(' ')

# Transform to integer
a = int(a, 16)
b = int(b, 16)

# Print a,b in Hexadecimal & binary
print("a = {0:#x} = {0:#010b}".format(a))
print("b = {0:#x} = {0:#010b}".format(b))

# Print after bit operation
print("a & b = {0:#x} = {0:#010b}".format(a & b))
print("a | b = {0:#x} = {0:#010b}".format(a | b))
print("a ^ b = {0:#x} = {0:#010b}".format(a ^ b))