x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

nList = [[0]*1000 for i in range(0,1000)]

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        nList[i][j] = 1

if nList[x3][y3] == 1:
    print("충돌")
else:
    print("비충돌")