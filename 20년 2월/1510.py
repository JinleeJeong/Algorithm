n = int(input())
nList = [[0]*n for i in range(n)]

count = 1
x = 0
y = n // 2

if n == 1:
    print(1)
else:
        
    while any(0 in x for x in nList):
        # print('x : ', x, 'y : ', y)
        nList[x][y] = count
        
        if count % n == 0:
            x += 1
            count += 1
        else:
            x -= 1
            y += 1
            
            if x == -1:
                x = n-1
            
            if y == n:
                y = 0

            count += 1

    for i in range(n):
        for j in range(n):
            print(nList[i][j], end=" ")

        print()