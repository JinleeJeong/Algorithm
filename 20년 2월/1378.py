n = int(input())

sumNum = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if(j > i):
            break
        else:
            sumNum += j

print(sumNum)