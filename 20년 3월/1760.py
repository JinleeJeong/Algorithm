nList = list(input())
cmpList = list(input())
numList = []

for i in cmpList:
    for j in range(10):
        # print('Here : ', i, nList[j])
        if i == nList[j]:
            numList.append(j)
            break
        elif i == " ":
            numList.append(" ")
            break
        else:
            continue

for x in numList:
    print(x, end="")