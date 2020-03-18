n = int(input())

cnt = 1
def numPrint(cnt):
    if cnt <= n:
        print(cnt, end=" ")
        cnt += 1
        numPrint(cnt)

numPrint(cnt)