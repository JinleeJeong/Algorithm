from math import *

n = int(input())

nList = []
distance = 0

for i in range(n):
    nList.append(list(map(int,input().split())))

for x in range(0, len(nList)-1):
    
    x1, y1 = nList[x][0], nList[x][1]
    x2, y2 = nList[x+1][0], nList[x+1][1]

    dx=x1-x2
    dy=y1-y2
    distance += sqrt(dx*dx + dy*dy)

print('%.2f'%distance)