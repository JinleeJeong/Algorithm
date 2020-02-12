n = int(input())
nList = []

for x in range(0, n):
    nList.append(input())
    
# 버블은 0~n 0~n-1로 비교 후 바로바로 위치 변경
for i in range(0, n):
    for j in range(0, n-1):
        if nList[j] > nList[j+1]:
            nList[j], nList[j+1] = nList[j+1], nList[j]

for y in nList:
    print(y)
