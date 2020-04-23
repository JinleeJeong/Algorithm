n = int(input())
nList = list(map(int, input().split()))
minList = []

for i in range(0, n):
    for j in range(1, n):
        if i != j:
            minList.append([nList[i], nList[j], abs(nList[i]+nList[j])])

minList = sorted(minList, key= lambda e: [e[2]])

print(minList[0][0], minList[0][1])