a, b = map(int, input().split())
sumNum = 0
for i in range(a, b+1):
    if i % 3 == 0 and i % 4 == 0:
        continue
    else:
        if i % 3 == 0:
            sumNum += i
        elif i % 4 == 0 :
            sumNum -= i
        else:
            continue

print(sumNum)