k, n = map(int,input().split())

nList = []
cnt = 0

for i in range(k):
    nList.append(list(map(int, input().split())))

for i in range(0, k):
    for j in range(0, k):
        if nList[i][j] + n < 6 and nList[i][j] != -1:
            cnt += 1

print(cnt)