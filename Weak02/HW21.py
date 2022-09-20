# HW21.py
"""
Project : Funtion of Circle
Author: Eun-seong Choi
Date of last update: 2022 / 9 / 14
Update list:
    - v1,1 : 9 /14
        Make a constant(PI)
        Make a variables(radius, circumference, area)
        Get circle data(radius)
        Add calc for circle data
        Add print for circle data
"""
# Constant
PI = 3.141592

# Get radius data
radius = int(input("Enter the radius(integer) : "))

# Calc the circle data
circumference = 2*PI*radius  # Circumference
area = PI*radius*radius  # Area

# Print circle data
print("Circumference : ", circumference)  # Circumference
print("Area : ", area)  # Area
