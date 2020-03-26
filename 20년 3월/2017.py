n, k = map(int, input().split())
nList = [0] * 10000
cnt = 0

if n == 0:
    print(0)
else:
    while n > 0:
        nList[cnt] = n%k
        cnt+=1
        n //= k
    cnt -= 1

    while cnt >= 0:
        if nList[cnt] >= 10:
            print(chr(nList[cnt]+55), end="")
            cnt -= 1
        else:
            print(nList[cnt], end="")
            cnt -= 1
