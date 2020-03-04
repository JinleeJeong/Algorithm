a,b,c = map(int, input().split())

nList = []
nList.append(a)
nList.append(b)
nList.append(c)

for i in range(0, 3):
    for j in range(0, 2):
        if nList[j] > nList[j+1]:
            nList[j], nList[j+1] = nList[j+1], nList[j]

for i in nList:
    print(i, end=" ")