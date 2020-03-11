n = int(input())
nList = list(map(int, input().split()))

for i in range(0, n):
    for j in range(0, n-1):
        if nList[j] < nList[j+1]:
            nList[j], nList[j+1] = nList[j+1], nList[j]

for i in nList:
    print(i, end= " ")