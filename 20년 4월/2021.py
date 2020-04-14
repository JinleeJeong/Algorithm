N = int(input())
maxNum = 0
minNum = 0
numDict = {}
frequency = []
frequencyNum = 0
for i in range(N):
    x = int(input())
    if numDict.get(x) != None:
        numDict.update({x : numDict.get(x) + 1})
    else:
        numDict.update({x : 1})
    # print(numDict)

res = sorted(numDict.items(), key=(lambda x:(x[1], x[0])), reverse=True)
# print(res)

absFlag = True
firstKey = res[0][0]
firstValue = res[0][1]

for i,j in numDict.items():
    if i == firstKey and j == firstValue:
        continue
    elif firstValue > j:
        if firstKey > i:
            # print(i)
            res = sorted(numDict.items(), key=(lambda x:(x[1], x[0])))
            break
    else:
        if firstKey > i:
            res = sorted(numDict.items(), key=(lambda x:(x[0], x[1])))
            absFlag = False
            break
# print(res)

if absFlag:
    # print(res)
    print(abs(firstKey-res[1][0]))
else:
    print(abs(firstKey - res[0][0]))
