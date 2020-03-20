import numpy as np

n = int(input())
nList = np.zeros((26, 26))

nList[1][1] = 1
print(int(nList[1][1]))
def pascal(x,y):
    if x > n:
        return
    elif y == 1:
        nList[x][y] = nList[x-1][y]
        print(int(nList[x][y]), end=" ")
        pascal(x, y+1)
    elif x == y:
        nList[x][y] = 1
        print(int(nList[x][y]))
        pascal(x+1, 1)
    else:
        nList[x][y] = nList[x-1][y-1] + nList[x-1][y]
        print(int(nList[x][y]), end=" ")
        pascal(x, y+1)

pascal(2,1)