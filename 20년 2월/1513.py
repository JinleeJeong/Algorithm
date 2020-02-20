n = int(input())

nList = [[0] * n for i in range(n)]

count = 0

# x의 시작 값, sw의 True False로 상승 하강 파악
x, y = n-1, 0
sw = True
for i in range(0, n):
# n번을 돌린다.
    if sw == True:
        # 상승으로 5, 3, 1번 반복
        for j in range(0, n-i):
            count += 1
            nList[x][y] = count
            # 마지막 일때, 전달 할 값
            if j == n-i-1:
                x += 1
                sw = False
            else:    
                x -= 1
                y += 1
            

    else:
        # 하강으로 4, 2 반복
        for j in range(0, n-i):
            count += 1
            nList[x][y] = count
            # 마지막 일때, 전달 할 값
            if j == n-i-1:
                y += 1
                sw = True
            else:    
                x += 1
                y -= 1
        
for i in range(n):
    for j in range(n):
        print(nList[i][j], end=" ")

    print()