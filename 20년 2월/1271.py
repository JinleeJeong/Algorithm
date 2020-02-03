n = int(input())
nList = list(map(int, input().split()))

maxNum = 0
for i in nList:
    if(maxNum < i):
        maxNum = i
print(maxNum)