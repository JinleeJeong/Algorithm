n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
count = 0

#0부터 3까지 0~4
for i in range(0, n+m-1): # 0 1 2 3 n+m-1인 이유는 2행 3열을 나타내기 때문에, 나열했을 때, i값과 같아야 함!!
    for j in range(0, m): # 0 1 2
        for k in range(0, n): # 0 1
            if j+k == i:
                
                count += 1
                matrix[k][j] = count

for i in range(0, n):
    for j in range(m-1, -1, -1):
        print(matrix[i][j], end=' ')
    print()