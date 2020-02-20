nList = []
horseStatus = []
for i in range(0, 10):
    nList.append(list(map(int, input().split())))

horseList = list(map(int, input().split()))

for x in range(0, 10):
    if horseList[x] == 1:
        for y in range(9, -1, -1):
            if nList[y][x] > 0:
                horseStatus.append([x+1, "crash"])
                break
            elif nList[y][x] < 0:
                horseStatus.append([x+1, "fall"])
                break
            else:
                if y == 0:
                    horseStatus.append([x+1, "safe"])

for i in range(0, len(horseStatus)):
    print(horseStatus[i][0], horseStatus[i][1])