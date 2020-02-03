n = int(input())
nList = list(map(int, input().split()))

nResult = 0

for i in nList:
    if(i % 5 == 0):
        nResult+=i

print(nResult)