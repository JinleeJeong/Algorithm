n = int(input())

cnt = 1
sumNum = 0

def sumDef(cnt):
    global sumNum

    if cnt <= n:
        sumNum += cnt
        cnt += 1
        sumDef(cnt)

sumDef(cnt)

print(sumNum)
