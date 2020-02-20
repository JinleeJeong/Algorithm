n = int(input())
nList = []
for i in range(n):
    nList.append([int(input())])

for x in range(1, n):
    for y in range(0, x):
        
        nList[x].append(nList[x][y]-nList[x-1][y])

for x in range(0, n):
    for y in nList[x]:
        print(y, end=" ")
    print()