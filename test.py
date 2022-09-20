# This is test file

# 1 = mon, 2 = tue

# 1년 > mon, 2년 tue...

# 서기 일년부터 계산하여 2022년의 시작 연도를 계산하는 프로그렘

count = 1
for i in range(1, 2022):
    if ((i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0)):
        count += 2
    else:
        count += 1
count %= 7
print(count)
