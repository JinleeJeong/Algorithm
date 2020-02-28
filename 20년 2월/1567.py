n = int(input())
nList = list(map(int,input().split()))
a, b = map(int ,input().split())

nSum = 0
for i in range(a-1, b):
    nSum += nList[i]

print(nSum)