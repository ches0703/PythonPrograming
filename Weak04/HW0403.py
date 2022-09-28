# HW0403.py
"""
Project : Get nation & it's capital and search with dict
Author: Eun-seong Choi
Date of last update: 2022 / 9 / 29
Update list:
    - v1,1 : 9 /29
        Make a part of Get nation & capital, and it save in dict
        Print dict
        Search nation's capital, and print value
"""
# Make empty dict
dict_nation_capital = {}


# Get nation & capital
while True:
    get_data = input("Input nation and its capital (. to quit) : ")
    # if user enter '.', end get nation & capital part
    if get_data == '.':
        break
    # key = nation, value = capital
    nation, capital = get_data.split(" ")
    dict_nation_capital[nation] = capital


# Print dict
print("dict_nation_capital : ", dict_nation_capital)


# Search nation's capital
while True:
    get_data = input("Input nation to find its capital (. to quit) : ")
    # if user enter '.', end search part
    if get_data == '.':
        break
    # Print value by key
    if get_data in dict_nation_capital:
        print("The capital of {} is {}".format(
            get_data, dict_nation_capital[get_data]))
    # Print if key is None in dict
    else:
        print("No Data...")
