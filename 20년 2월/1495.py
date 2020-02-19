n, m, k = map(int,input().split())

# List는 0부터 시작하고, e는 1부터 이며 +1까지 이므로, 2로 nList 적용
# 배열 1000개씩 할당 해야함.. 아래의 x,y 좌표들의 변수가 존재 하기 때문!!
nList = [[0] * (n+1000) for x in range(0,m+1000)]
count = 0

for i in range(0, k):
    x1, y1, x2, y2, u = map(int, input().split())

    nList[x1][y1] += u
    nList[x2+1][y2+1] += u

    nList[x1][y2+1] -= u
    nList[x2+1][y1] -= u

for x in range(0, n):
    for y in range(0, m):
        print(nList[x][y], end=" ")
    
    print()

print()

# 가로 축 누적 합 적용
for i in range(0, n):
    for j in range(0, m):
        if i == 0 and j == 0:
            count += nList[i][j]
        else:
            nList[i][j] += count
            count = nList[i][j]
    count = 0

# 세로 축 누적 합 적용 
for i in range(1, len(nList)):
    for j in range(0, len(nList[i])):
        nList[i][j] += nList[i-1][j]

for i in range(0, n):
    for j in range(0, m):
        print(nList[i][j], end=" ")
    print()
