a, b = map(int ,input().split())

cnt = 0
for i in range(a, b+1):
    j = i
    

    while j > 0:
        if j % 10 == 1:
            cnt += 1
        j //= 10

print(cnt)