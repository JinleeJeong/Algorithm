n, m = map(int, input().split())

nmList = []

for i in range(0, n):
    nmList.append(list(map(int, input().split())))

for i in range(0, n):
    for j in range(0, m):
        print(nmList[i][j], end=" ")
    print()