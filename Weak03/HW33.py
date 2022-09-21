# HW33.py
"""
Project : Total date calculator
Author: Eun-seong Choi
Date of last update: 2022 / 9 / 21
Update list:
    - v1,1 : 9 /21
        Setting basic list
        Calc now month's first day's day of the weak
        Setting max days
        Print calecder with Sun start
    - v1.2 : 9 /22
        Fix print sentancs

"""
# Setting basic list
day_of_the_weak = ["Mon", "Tue", "Wed", "Thu",
                   "Fri", "Sat", "Sun"]  # Day of the weak name
months_of_12 = ["Jan", "Fab", "Mar", "Apr", "May",
                "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  # Months name
months_of_31days = [1, 3, 5, 7, 8, 10, 12]  # Months with 31days


# Calc first day's day of the weak
year, month, day = map(int, input("Enter year, month, day : ").split(' '))
# Calc year's first day's day of weak :
# if N year's Jan 01 is on Monday,
# N + 1 year's Jan 01 is Tuesday (when N year is not leap year)
position_of_1st = year-1
for i in range(1, year):
    # Check Leap year
    if ((i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0)):
        # Else if N year is Leap year, N + 1 year's Jan 01 is Wednesday
        position_of_1st += 1


# Calc month's first day's day of weak :
# It simular calc year's first day's day of weak
for i in range(1, month):
    if (i in months_of_31days):
        position_of_1st += 3
    elif (i == 2):  # Check Feb
        # Check Leap year
        if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
            position_of_1st += 1
    else:
        position_of_1st += 2


# Calc index of day_of_weak
position_of_1st %= 7
position_of_1st += 1  # For print start sunday


# Setting max day
if (month in months_of_31days):
    max_days = 31
elif (i == 2):  # Check Feb
    # Check Leap year
    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        max_days = 29
    else:
        max_days = 28
else:
    max_days = 30

# Print calender title
print()
print("{} of year {}".format(months_of_12[month-1], year))
print("===========================")
# Print day of the weak to start Sun
print(day_of_the_weak[6], end=' ')  # Print Sun
for i in range(0, 6):  # Print else
    print(day_of_the_weak[i], end=' ')
print()
print("---------------------------")
# Print days
day_count = 1
for i in range(6):
    for j in range(7):
        if (day_count > max_days):
            break
        if ((i == 0) and (j < position_of_1st)):
            print("   ", end=' ')  # Print blank before first day
        else:
            print(format(day_count, '3d'), end=' ')
            day_count += 1
    print()  # Start in new line
print("===========================")
