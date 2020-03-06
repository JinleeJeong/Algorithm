n = list(input())

sumNum = 0
for i in n:
    sumNum += int(i)

if sumNum % 7 == 4:
    print("Bad")
else:
    print("Good")