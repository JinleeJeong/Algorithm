n = int(input())
nList = [[0]*n for i in range(n)]
count = 0
result = 0

if n == 1:
    print(1)
elif n == 2:
    print(10)
else:
    for i in range(n):
        for j in range(n):
            count += 1
            nList[i][j] = count

    x = 0
    y = 0

    count = 0

    for i in range(n):
        result += nList[0][i]
        y = i

    for i in range(n):
        if i != 0:
            result += nList[i][y]    
            x = i

    for i in range(n-1, -1, -1):
        if i != n-1:
            result += nList[x][i]
            y = i

    for i in range(n-1, -1, -1):
        if i != n-1 and i != 0:
            result += nList[i][y]

    print(result)