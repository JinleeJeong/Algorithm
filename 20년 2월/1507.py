matrix = [[0]*8 for i in range(8)]
cnt = 0

for i in range(0, 4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2): # 2 5
        for y in range(y1, y2): # 3 7
            matrix[x][y] = 1 # 2,3 2,4 2,5 2,6 3,3 3,4 3,5 3,6 ~ 5,6

for i in range(0, 8):
    for j in range(0, 8):
        print(matrix[i][j], end=" ")
        if matrix[i][j] == 1:
            cnt += 1
    print()
print(cnt)