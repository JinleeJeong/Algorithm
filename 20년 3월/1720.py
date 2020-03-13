n = int(input())
nList = []
nFlag = False

for i in range(n):
    nList.append(list(map(int,input().split())))

for x in range(0, len(nList)):
    
    minNum = nList[x][len(nList[x])-1]
    
    if minNum not in nList[x][0:3]:
        print(x+1, min(nList[x][0:3]))
        nFlag = True
    else:
        for y in range(0, len(nList[x])-1):
            
            if nList[x][y] < minNum:
                minNum = nList[x][y]

        if minNum == nList[x][len(nList[x])-1]:
            continue
        else:
            print(x+1, minNum)
            nFlag = True

if nFlag == False:
    print(-1)

