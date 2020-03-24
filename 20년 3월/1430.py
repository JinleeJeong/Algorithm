N = int(input())
NList = list(map(int,input().split()))
arr = [0] * 10000001
for i in range(N):
    arr[NList[i]] = 1

M = int(input())
MList = list(map(int, input().split()))

for j in MList:
    print("%d "%arr[j], end="")