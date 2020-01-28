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
            # x 값이 changeTime[0] 값 즉 바꾸는 행의 값과 같으면 반대 값을 넣어준다(뒤집기)
            if(x == (changeTime[0]-1)):

                if(stage[x][y] == 1):
                    stage[x][y] = 0
                else:
                    stage[x][y] = 1
            # y 값이 changeTime[1] 값 즉 바꾸는 열의 값과 같으면 반대 값을 넣어준다(뒤집기)
            if(y == (changeTime[1]-1)):

                
                if(stage[x][y] == 1):
                    stage[x][y] = 0
                else:
                    stage[x][y] = 1

for i in range(0, 19):
    for j in range(0, 19):
        # 19개를 출력 후, 줄 바꿈 Prettier
        if(i > count):
            print("")
            count += 1
        print(stage[i][j], end=" ")