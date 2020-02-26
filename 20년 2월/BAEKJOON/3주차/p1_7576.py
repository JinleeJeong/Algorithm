# bfs 문제.. 너비 우선 탐색

import copy
import sys

n, m = map(int, sys.stdin.readline().split())
nList = []
cnt = 0
listFlag = False
for i in range(0, m):
    nList.append(list(map(int, sys.stdin.readline().split())))

while any(0 in x for x in nList):
# for x in range(0, 2):
    supList = copy.deepcopy(nList)
    for i in range(0, m): # 4
        for j in range(0, n): # 6
            if supList[i][j] == 1:

                try: 
                    if supList[i-1][j] == 0 and i-1 > -1 :
                        # print("true 1", i-1, j)
                        nList[i-1][j] = 1
                        listFlag = True
                except IndexError:
                    pass
                
                try: 
                    if supList[i][j-1] == 0 and j-1 > -1:
                        # print("true 2", i, j-1)
                        nList[i][j-1] = 1
                        listFlag = True
                except IndexError:
                    pass

                try: 
                    if supList[i+1][j] == 0 and i+1 < m :
                        # print("true 3" , i+1, j)
                        nList[i+1][j] = 1
                        listFlag = True
                except IndexError:
                    pass

                try: 
                    if supList[i][j+1] == 0 and j+1 < n:
                        # print("true 4", i, j+1)
                        nList[i][j+1] = 1
                        listFlag = True
                except IndexError:
                    pass
                
            else:
                continue

    if nList == supList:
        listFlag = False
        break
    else:
        listFlag = True

    cnt += 1
    supList = nList

if listFlag:
    print(cnt)
else:
    print(-1)