n = int(input())
nList = list(map(int, input().split()))

cnt = 0

if n == 1:
    if nList[0] == 0:
        print(1)
    else:
        print(0)
else:
    for i in range(0, n):
        if i-1 < 0:
            if nList[i] == 0 and nList[i+1] == 0:
                cnt+= 1
            else:
                continue
        elif i+1 == n:
            if nList[i] == 0 and nList[i-1] == 0:
                cnt+= 1
            else:
                continue
        else:
            if nList[i-1] == 0 and nList[i+1] == 0 and nList[i] == 0:
                cnt += 1

    print(cnt)