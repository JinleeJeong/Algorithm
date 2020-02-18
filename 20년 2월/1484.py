# 달팽이 채우기
# 1 2 3 4
# 10 11 12 5
# 달팽이 문제!!

# 1 2 3 4 5
# 14 15 16 17 6
# 13 20 19 18 7
# 12 11 10 9 8

n, m = map(int, input().split()) # 4, 5
matrix = [[0]*m for i in range(n)]

x,y = 0,0
xm, ym = 1, 1
count = 0

while any(0 in x for x in matrix):
    if xm == 1:    
        for i in range(0, m):
            if matrix[x][i] == 0:
                count += 1
                matrix[x][i] = count
                y = i
                xm = -1

    else:
        for i in range(m-1, -1, -1):
            if matrix[x][i] == 0:
                count += 1
                matrix[x][i] = count
                y = i
                xm = 1
                
    if ym == 1:
        for j in range(0, n):
            if matrix[j][y] == 0:
                count += 1
                matrix[j][y] = count
                x = j
                ym = -1

    else:
        for j in range(n-1, -1, -1):
            if matrix[j][y] == 0:
                count += 1
                matrix[j][y] = count
                x = j
                ym = 1

for i in range(0, n):
    for j in range(0, m):
        print(matrix[i][j], end=' ')
    print()
