# input
# 3 5
# 1 2 3 4 5 
# 5 4 3 2 1 
# 1 5 2 4 3 

# output 누적 합 데이타!
# 1 3 6 10 15 
# 6 12 18 24 30 
# 7 18 26 36 45 

n, m = map(int, input().split())
nList = []

for i in range(0, n):
    nList.append(list(map(int, input().split())))

newList = []
forList = []
count = 0

# 가로 축 누적 합 적용
for x in range(0, len(nList)):
    for y in nList[x]:
        if y == 0:
            forList.append(y)
            count += y
        else:
            count += y
            forList.append(count)
    newList.append(forList)
    forList = []
    count = 0

# 세로 축 누적 합 적용 
# [[1, 3, 6, 10, 15], [5, 9, 12, 14, 15], [1, 6, 8, 12, 15]]
for x in range(1, len(newList)):
    for y in range(0, len(newList[x])):
        newList[x][y] += newList[x-1][y]
# [[1, 3, 6, 10, 15], [6, 12, 18, 24, 30], [7, 18, 26, 36, 45]]

for x in range(0, len(newList)):
    for y in newList[x]:
        print(y, end=" ")
    print()
