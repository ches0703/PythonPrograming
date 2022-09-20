# Training Conditional Expression

score = int(input("Enter your score : "))
if 80 < score < 100:
    print("A")
elif 60 < score:
    print("B")
elif 40 < score:
    print("C")
else:
    print("F")


year = int(input("Enter year : "))
if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    print("Leap Year", year)
else:
    print("That is not Leaf Year")
