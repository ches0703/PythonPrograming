# Training For Loop

s = "Apple is delicious"
count = 0
for i in s:
    if (i == 'e'):
        count += 1
print("'e''s count in stirng : ", count)

for i in range(1, 10):
    for j in range(1, 10):
        print("{} x {} = {:2}".format(i, j, i*j), end='  ')
    print()
