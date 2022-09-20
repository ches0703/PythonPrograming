# HW22.py
"""
Project : Funtion of Rect
Author: Eun-seong Choi
Date of last update: 2022 / 9 / 14
Update list:
    - v1,1 : 9 /14
        Make a variables(width, length, perimeter, area)
        Get rect data(width,, length)
        Add calc for rect data
        Add print for rect data
"""
# Get rect data
width = int(input("Enter the width(integer) : "))  # Width
length = int(input("Enter the length(integer) :"))  # Length

# Calc the rect data
perimeter = 2*width+2*length  # Perimeter
area = width*length  # Area

# Print rect data
print("Rect's perimeter : ", perimeter)  # Perimeter
print("Rect's area : ", area)  # Area
