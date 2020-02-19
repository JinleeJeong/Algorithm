# 달팽이 채우기
# 달팽이 문제!!

n = int(input())
matrix = [[0]*n for i in range(n)]

x,y = 0,0
xm, ym = 1, 1
count = 0

# matrix가 0이 없을때 까지 반복!!
while any(0 in x for x in matrix):

    if ym == 1: # 아래로
        for j in range(0, n):
            if matrix[j][y] == 0:
                count += 1
                matrix[j][y] = count
                x = j
                ym = -1

    else: # 위로
        for j in range(n-1, -1, -1):
            if matrix[j][y] == 0:
                count += 1
                matrix[j][y] = count
                x = j
                ym = 1

    if xm == 1:    # 가로로 정상
        for i in range(0, n):
            if matrix[x][i] == 0:
                count += 1
                matrix[x][i] = count
                y = i
                xm = -1

    else: # 가로로 반대로
        for i in range(n-1, -1, -1):
            if matrix[x][i] == 0:
                count += 1
                matrix[x][i] = count
                y = i
                xm = 1
                
    
for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end=' ')
    print()
