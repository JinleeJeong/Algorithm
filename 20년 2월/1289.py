aList = list(map(int,input().split()))
bList = list(map(int,input().split()))
cList = list(map(int,input().split()))

maxNum = 0

aResult = aList[0]*aList[1]
bResult = bList[0]*bList[1]
cResult = cList[0]*cList[1]    

if(aResult > bResult):
    if(aResult > cResult):
        print(aResult)
    else:
        print(cResult)
else:
    if(bResult > cResult):
        print(bResult)
    else:
        print(cResult)

