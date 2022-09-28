t_ch = 'a', 'b', 'c'
t_ascii = 97, 98, 99
print("t_ch : ", t_ch)
print("t_ascii : ", t_ascii)
t_zip = list(zip(t_ch, t_ascii))
print(t_zip)
for i in t_zip:
    print(i)

t1 = 3, 45, 6, 6, 3, 2
t1 = sorted(t1)
print(t1)
