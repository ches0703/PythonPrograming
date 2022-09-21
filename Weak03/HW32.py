
year, month, day = map(int, input("Enter year : ").split(' '))

day_of_the_weak = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months_of_12 = ["Jan", "Fab", "Mar", "Apr", "May",
                "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
months_of_31days = [1, 3, 5, 7, 8, 10, 12]

total_days = (year-1) * 365
for i in range(1, year):
    if ((i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0)):
        total_days += 1

for i in range(1, month):
    if (i in months_of_31days):
        total_days += 31
    elif (i == 2):
        if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
            total_days += 29
        else:
            total_days += 28
    else:
        total_days += 30


total_days += day

print(day_of_the_weak[total_days % 7 - 1])
print(total_days)
