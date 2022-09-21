# HW32.py
"""
Project : Total date calculator
Author: Eun-seong Choi
Date of last update: 2022 / 9 / 21
Update list:
    - v1,1 : 9 /21
        Setting basic list
        Enter iterator
        Get data(year, month, day)
        Calc data(year, month, day to total days)
        Print inpuy data & resulte

"""
# Setting basic list
day_of_the_weak = ["Mon", "Tue", "Wed", "Thu",
                   "Fri", "Sat", "Sun"]  # Day of the weak name
months_of_12 = ["Jan", "Fab", "Mar", "Apr", "May",
                "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  # Months name
months_of_31days = [1, 3, 5, 7, 8, 10, 12]  # Months with 31days


# Start infinity iterator
while True:

    # Get data(year, month, day)
    year, month, day = map(int, input("Enter year, month, day : ").split(' '))
    if ((year == 0) and (month == 0) and (day == 0)):  # To stop iterator
        print("End program")
        break

    # Calc year to days
    total_days = (year-1) * 365  # Calc Until last year
    # Additional calc by Leap year
    for i in range(1, year):
        # Check Leap year
        if ((i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0)):
            total_days += 1

    # Calc month to days
    for i in range(1, month):  # Calc Until last month
        if (i in months_of_31days):  # Check now month has 31days
            total_days += 31
        elif (i == 2):  # Check Feb
            # Check Leap year
            if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
                total_days += 29
            else:
                total_days += 28
        else:
            total_days += 30

    # Calc day to days
    total_days += day

    # Print inpuy data & resulte
    # Print input data
    print("{} {} in AD {} : ".format(
        months_of_12[month-1], day, year), end='')
    # Print day of weak and total days
    print("Weak_day({}), elapsed {} days from Jan 01 in AD 1 : ".format(
        day_of_the_weak[total_days % 7 - 1], total_days))
