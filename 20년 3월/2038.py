myShiledList = list(map(int, input().split()))
myShiled = 0
mySword = int(input())
portion = list(input().split())

finishFlag = False
for i in myShiledList:
    myShiled += i

enemy = list(map(int, input().split()))

enemySword = enemy[0]
enemyShiled = enemy[1]

if portion[0] == '1':
    if len(portion) == 4:
        if portion[1] == '+':
            mySword += int(portion[2])
        else:
            mySword *= int(portion[2])
    else:
        if portion[1][0] == '+':
            mySword += int(portion[1][1])
        else:
            mySword *= int(portion[1][1])

    while True:

        if finishFlag == True:
            break
        for i in range(0, int(portion[2])):           
            if finishFlag == False:
                enemyShiled -= mySword

                if enemyShiled < 0:
                    finishFlag = True
                    print(1)
                else:
                    myShiled -= enemySword

                    if myShiled < 0:
                        finishFlag = True
                        print(0)
            else:
                break
else:   
    while True:

        if finishFlag == True:
            break       
        if finishFlag == False:
            enemyShiled -= mySword

            if enemyShiled < 0:
                finishFlag = True
                print(1)
            else:
                myShiled -= enemySword

                if myShiled < 0:
                    finishFlag = True
                    print(0)
        else:
            break