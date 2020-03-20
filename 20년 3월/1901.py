n = int(input())
cnt = 1

def printNum(cnt):
    if cnt > n:
        return
    else:
        print(cnt)
        cnt += 1
        printNum(cnt)

printNum(cnt)