m, n, x, y = map(int, input().split())
nList = []
ka = 0


for i in range(n):
    nList.append(list(map(int, input().split())))

for i in range(n-y+1):
    for j in range(m-x+1):
        sumNum = 0
        
        for k in range(i, i+y):
            for l in range(j, j+x):
                sumNum += nList[k][l]

        if ka < sumNum:
            ka = sumNum

print(ka)
