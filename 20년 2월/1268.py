n = int(input())
nList = list(map(int, input().split()))

nResult = 0

for i in nList:
    if(i % 2 == 0):
        nResult+=1

print(nResult)