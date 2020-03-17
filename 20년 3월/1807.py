a, b = map(int, input().split())
maxNum = 0
maxidx = 0
for i in range(a, b+1):
    # print(i, end=" ")
    cnt = 0
    n = i
    while True:
        if n == 1:
            cnt += 1
            if maxNum < cnt:
                maxNum = cnt
                maxidx = i
            break
        else:
            cnt += 1
            if n % 2 == 1:
                n = 3*n+1
            else:
                n //= 2
print(maxidx, maxNum)