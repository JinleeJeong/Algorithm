n = int(input())
nList = list(map(int, input().split()))

resultList = []
for i in range(0, len(nList), 2):
    if nList[i] < nList[i+1]:
        resultList.append(nList[i+1])
    else:
        resultList.append(nList[i])

for i in resultList:
    print(i, end=" ")