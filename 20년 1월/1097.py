count = 0
# 바둑판 배열 만들기
stage = []
for i in range(0, 19):
    row = list(map(int, input().split(" ")))
    stage.append(row)

n = int(input())
# 뒤집기 할 갯수 지정

for i in range(0, n):
    changeTime = list(map(int,input().split(" ")))

    for x in range(0, 19):
        for y in range(0, 19):

            if(x == (changeTime[0]-1)):

                if(stage[x][y] == 1):
                    stage[x][y] = 0
                else:
                    stage[x][y] = 1
            if(y == (changeTime[1]-1)):

                
                if(stage[x][y] == 1):
                    stage[x][y] = 0
                else:
                    stage[x][y] = 1

for i in range(0, 19):
    for j in range(0, 19):
        if(i > count):
            print("")
            count += 1
        print(stage[i][j], end=" ")