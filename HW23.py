# HW23.py
"""
Project : Print Decimal, Binary, Octal, Hexadecimal in 0 to 255
Author: Eun-seong Choi
Date of last update: 2022 / 9 / 14
Update list:
    - v1,1 : 9 /14
        Make a variables(width, length, perimeter, area)
        Get rect data(width,, length)
        Add calc for rect data
        Add print for rect data
"""

for i in range(0, 256):  # Iterate i = 0 to i = 255
    print(
        " Dec:", format(i, '3'),     # Decimal
        " Bin:", format(i, '#10b'),  # Binary
        " Oct:", format(i, '#5o'),   # Octal
        " Hex:", format(i, '#4x')    # Hexadecimal
    )
