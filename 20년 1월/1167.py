numList = list(map(int, input().split(" ")))

maxNum = 0
minNum = 10000

for i in numList:
    if(i > maxNum):
        maxNum = i
    if(i < minNum):
        minNum = i

print(numList[0]+numList[1]+numList[2]-maxNum-minNum)