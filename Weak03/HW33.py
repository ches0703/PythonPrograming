

year, month, day = map(int, input("Enter year : ").split(' '))

day_of_the_weak = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months_of_12 = ["Jan", "Fab", "Mar", "Apr", "May",
                "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
months_of_31days = [1, 3, 5, 7, 8, 10, 12]
position_of_1st = year-1
for i in range(1, year):
    if ((i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0)):
        position_of_1st += 2


for i in range(1, month):
    if (i in months_of_31days):
        position_of_1st += 3
    elif (i == 2):
        if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
            position_of_1st += 1
    else:
        position_of_1st += 2

position_of_1st %= 7
position_of_1st += 1  # for start sunday
day_count = 1
for i in range(6):
    for j in range(7):
        if ((i == 0) and (j >= position_of_1st)):
            print(format(day_count, '2d'), end=' ')
            day_count += 1
        elif (i == 0):
            print("  ", end=' ')
        else:
            print(format(day_count, '2d'), end=' ')
            day_count += 1

    print()
