n = int(input())
nList = []
mapList = [['.'] * 60 for i in range(30)]
for i in range(n):
    nList.append(input().split())

# print(nList)

for i in range(0, len(nList)):
    # print(i)
    textList = list(nList[i][0])
    # print('text : ',textList)
    for x in range(int(nList[i][2])-1, int(nList[i][4])):
        for y in range(int(nList[i][1])-1, int(nList[i][3])):
            
            if x == int(nList[i][2])-1 and y == int(nList[i][1])-1 or x == int(nList[i][2])-1 and y == int(nList[i][3])-1 or x == int(nList[i][4])-1 and y ==int(nList[i][1])-1 or x == int(nList[i][4])-1 and y == int(nList[i][3])-1 :
                mapList[x][y] = "+"    
            
            elif x == int(nList[i][2])-1 and y == int(nList[i][1]):
                for z in textList:
                    if y == int(nList[i][3]):
                        break
                    else:
                        mapList[x][y] = z

                        y += 1
            
            elif x == int(nList[i][2])-1 and y >= len(textList) + int(nList[i][1]):

                mapList[x][y] = '-'
            elif x == int(nList[i][4])-1 :
                mapList[x][y] = '-'
            elif y == int(nList[i][1])-1 or y == int(nList[i][3])-1:
                mapList[x][y] = '|'
            elif mapList[x][y] not in textList or x > int(nList[i][2])-1 and y > int(nList[i][1])-1 :
                mapList[x][y] = " "

    textList = []
for i in range(30):
    for j in range(60):
        print(mapList[i][j], end="")
    print()