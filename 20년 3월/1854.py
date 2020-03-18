nList =list(input())
sumNum = 0
cnt = 0

def sumDef(nList, cnt):
    global sumNum

    if len(nList) > cnt:
        sumNum += int(nList[cnt])
        cnt += 1
        sumDef(nList, cnt)

sumDef(nList, cnt)

print(sumNum)
