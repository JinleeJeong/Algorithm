n = int(input())
nList = list(map(int, input().split()))
a = [0] * 100000

for i in range(0, len(nList)):
    
    a[nList[i]] += 1

for i in range(0, 100010):
    for j in range(0, a[i]):
        print(i, end=" ")
