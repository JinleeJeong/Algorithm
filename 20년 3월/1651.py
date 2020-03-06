w, h, n = map(int, input().split())

nList = []

for i in range(n):
    nList.append(list(input()))

# print(nList)

for i in range(0, n):
    for j in range(0, len(nList[i])):
        nList[i][j] *= w


for i in range(n):
    for x in range(h):
        for j in range(0, len(nList[i])):
            print(nList[i][j], end="")
        
        print()