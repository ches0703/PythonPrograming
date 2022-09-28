# HW0401.py
"""
Project : List of date tuples
Author: Eun-seong Choi
Date of last update: 2022 / 9 / 29
Update list:
    - v1,1 : 9 /29
        Make a list to save tuple
        Make a part that convert string to tuple
        Print, and sort list

"""
# Make empty list
L_dates = []


# Iter 10 times
for i in range(10):
    # Convert string to tuple
    data_tuple = tuple(
        map(int, (input("Input year, month, day : ").split(sep=" "))))
    # Save tuple in list
    L_dates.append(data_tuple)
    # Print to check saving
    print("L dates : ", L_dates)


# Print before sort
print("After input of 10 dates : ", L_dates)
# Sort list
L_dates.sort()
# Print after sort
print("After sorting L_dates : ", L_dates)
