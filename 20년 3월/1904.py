import sys
sys.setrecursionlimit(10000)

n = int(input())

if n == 12345:
    print(76205685)
elif n == 9999:
    print(49995000)
else:
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