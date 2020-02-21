matrix = [[0]*7 for i in range(7)]

# 가로 줄 채우기 4행!
for i in range(0, 7):
    matrix[3][i] = 1


nList = []
for i in range(3):
    nList.append(list(map(int, input().split())))


# x가 4인 경우는 확인 후, 세로 줄 1로 채워넣기 ★★ 4인경우 먼저!!!
for i in range(3):
    x, y = nList[i][0], nList[i][1]

    if x == 4:
        
        for i in range(0, 7):
            matrix[i][y-1] = 1

# 최소 2번을 돌면서 1의 값으로 업데이트 된 경우가 존재!! 
# Ex) 4,1 7,7 7,1이 있는데, 7,7은 0이였다가, 7,1이 적용된 후 1이되서 채워짐!!!
# 스플리트는 순서가 없어야 하기 때문에 2번 돌린다.

for index in range(2):
    for i in range(3):
        x, y = nList[i][0], nList[i][1]

        if matrix[x-1][y-1] == 1:
            for i in range(0, 7):
                matrix[x-1][i] = 1
                matrix[i][y-1] = 1

    # 맨 마지막에 2의 값 스플리터 입력
    
for i in range(3):
    matrix[nList[i][0]-1][nList[i][1]-1] = 2

for i in range(0, 7):
    for j in range(0, 7):
        print(matrix[i][j], end=' ')
    print()