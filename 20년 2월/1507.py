# 4개의 직사각형 넓이 구하기

matrix = [[0]*100 for i in range(100)]
cnt = 0

for i in range(0, 4):
    x1, y1, x2, y2 = map(int, input().split())

    # x1 ~ x2
    # y1 ~ y2의 값을 배열 접근 후 1로 대입

    for x in range(x1, x2): # 2 5
        for y in range(y1, y2): # 3 7
            matrix[x][y] = 1 # 2,3 2,4 2,5 2,6 3,3 3,4 3,5 3,6 ~ 5,6

for i in range(0, 100):
    for j in range(0, 100):
        if matrix[i][j] == 1:
            cnt += 1

print(cnt)