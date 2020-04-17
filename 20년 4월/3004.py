import copy

n = int(input())
nList = list(map(int, input().split()))
mList = copy.copy(nList)
mList = sorted(mList)
cnt = 0

for i in range(n):
    for j in range(n):
        if mList[i] == nList[j]:
            nList[j] = cnt
            cnt += 1
            break

for i in nList:
    print(i, end=" ")
