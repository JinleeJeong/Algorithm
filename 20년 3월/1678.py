nList = []
sumList = []

yy = 0
for i in range(5):
    nList.append(list(map(int,input().split())))

for x in range(3):
    sumNum = 0
    xx = x

    for y in range(3):
        sumNum += nList[xx][yy]
        sumNum += nList[xx+1][yy]
        sumNum += nList[xx+2][yy]
        
        yy += 1

    sumList.append(sumNum)
    
    yy = 1
    sumNum = 0
    for y in range(3):
        sumNum += nList[xx][yy]
        sumNum += nList[xx+1][yy]
        sumNum += nList[xx+2][yy]
        
        yy += 1

    sumList.append(sumNum)
    
    yy = 2
    sumNum = 0
    for y in range(3):
        sumNum += nList[xx][yy]
        sumNum += nList[xx+1][yy]
        sumNum += nList[xx+2][yy]
        
        yy += 1
    sumList.append(sumNum)

    yy = 0
print(max(sumList))