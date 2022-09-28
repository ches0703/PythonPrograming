L_dates = []

for i in range(10):

    data_tuple = tuple(
        map(int, (input("Input year, month, day : ").split(sep=" "))))
    
    L_dates.append(data_tuple)
    print("L dates : ", L_dates)

print("After input of 10 dates : ", L_dates)
L_dates.sort()
print("After sorting L_dates : ", L_dates)
