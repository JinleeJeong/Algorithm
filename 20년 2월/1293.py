n = int(input())
nList = list(map(int, input().split()))
maxNum = 0
minNum = 100
for i in nList:
    if(maxNum < i):
        maxNum = i
    if(minNum > i):
        minNum = i

print(maxNum, minNum, sep=" ")
