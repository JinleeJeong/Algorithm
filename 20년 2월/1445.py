n, m = map(int, input().split())

nList = list(map(int, input().split()))
mList = list(map(int, input().split()))

resultList = nList + mList

for i in range(0, len(resultList)):
    for j in range(0, len(resultList)-1):
        if(resultList[j] > resultList[j+1]):
            resultList[j], resultList[j+1] = resultList[j+1], resultList[j]

for x in resultList:
    print(x, end=" ")