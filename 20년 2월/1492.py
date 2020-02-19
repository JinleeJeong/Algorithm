n = int(input())
nList = list(map(int, input().split()))

newList = []
count = 0

for i in range(0, len(nList)):
    if i == 0:
        newList.append(nList[i])
        count += nList[i]
    else:
        count += nList[i]
        newList.append(count)

for i in newList:
    print(i, end=" ")