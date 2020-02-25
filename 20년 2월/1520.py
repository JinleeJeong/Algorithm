n, m = map(int, input().split())
x, y, z = map(int ,input().split())

nList = [[0]*(172) for i in range(172)]
mList = [[0]*(172) for i in range(172)]


for i in range(1, n+1):
    sup = list(map(int, input().split()))
    for j in range(0, m):
        nList[i][j+1] = sup[j]

k = int(input())

for i in range(0, k):
    for i in range(1, n+1):
        for j in range(1, m+1):
            life = nList[i-1][j-1] + nList[i][j-1] + nList[i+1][j-1] + nList[i-1][j] + nList[i+1][j] + nList[i-1][j+1] + nList[i][j+1] + nList[i+1][j+1]
            if nList[i][j] == 0:
                if life == x:
                    mList[i][j] = 1 
                else:
                    mList[i][j] = 0
            else:
                if life >= y and life < z:
                    mList[i][j] = 1 
                else: 
                    mList[i][j] = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        print(mList[i][j], end=' ')
    print()