n = int(input())
nList = list(map(int,input().split()))

for i in range(0, n):
    for j in range(0, n):
        print(nList[j], end=" ")
    nList.append(nList[0])
    nList.pop(0)
    print(" ")
    