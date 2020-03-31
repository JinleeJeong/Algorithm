strNum = list(input())

strDict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

sumNum = 0
if strDict.get(strNum[3]) > strDict.get(strNum[1]):
    sumNum -= int(strNum[0]) * strDict.get(strNum[1])
else:
    sumNum += int(strNum[0]) * strDict.get(strNum[1])

for i in range(2, len(strNum), 2):
    # print("hi")
    if i+3 < len(strNum):
        if strDict.get(strNum[i+3]) > strDict.get(strNum[i+1]):
            sumNum -= int(strNum[i]) * strDict.get(strNum[i+1])
        else:
            sumNum += int(strNum[i]) * strDict.get(strNum[i+1])
    else:
        sumNum += int(strNum[i]) * strDict.get(strNum[i+1])
    print(sumNum)

print(sumNum)