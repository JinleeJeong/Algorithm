n = int(input())
nList = []

for i in range(n):
    nList.append(list(map(int, input().split())))

nList.sort(key = lambda x: x[0])

for i in nList:
    print(i[0], i[1])