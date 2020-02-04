numList = []

for x in range(0,5):
    numList.append(int(input()))
maxNum = -1000000
minNum = 1000000
for i in numList:
    if(i > maxNum):
        maxNum = i
    if(i < minNum):
        minNum = i

print(maxNum, minNum, sep="\n")