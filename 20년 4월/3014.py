n = int(input())
nList = []
a = [0] * 100000

for i in range(0, n):
    nList.append(input())

for i in range(0, len(nList)):
    
    a[nList[i]] += 1

for i in range(0, 100010):
    for j in range(0, a[i]):
        print(i, end=" ")
