nList = list(input())

resultList = [''] * 1000
resultCnt = 0

for i in range(0, len(nList)):
    if nList[i] == ';' or nList[i] == ',':

        resultCnt += 1
        resultList[resultCnt] += str(nList[i])
        resultCnt += 1
    elif nList[i] == ' ':
        continue
    else:
        resultList[resultCnt] += str(nList[i])


for i in resultList:
    if i == ';':
        print()
    elif i == ',' or i == '':
        continue
    else:
        print(i, end=" ")