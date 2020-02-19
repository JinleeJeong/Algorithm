n = int(input())

flag = 1
count = 0
resultList = []
forList = []
for i in range(0,n):
    if flag == 1 :
        if i != 0: 
            count += n
        for j in range(0, n):
            count += 1
            forList.append(count)
            
        flag = -1
        resultList.append(forList)
        forList = []
    else:
        count += n
        for j in range(n-1, -1, -1):
            forList.append(count)
            
            count -= 1
        flag = 1
        resultList.append(forList)
        forList = []

for i in range(0, n):
    for j in range(0, n):
        print(resultList[j][i], end=" ")
    print()