numList = list(map(int, input().split()))

numFlag = 0
for i in numList:
    if(i % 5 == 0):
        numFlag = i
        break

if(numFlag):
    print(numFlag)
else:
    print(0)
        