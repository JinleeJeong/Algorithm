n = int(input())
nList = []

for i in range(n):
    nList.append(list(map(int, input().split())))
    nList[i].append(i+1)

# print(nList)
nList = sorted(nList, key=lambda e: (-e[0], -e[1]))

for i in nList:

    print(i[2], i[0], i[1], end="")
    print()