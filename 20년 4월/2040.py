nList = list(map(int, input().split()))
cnt = 0 

for i in range(0, len(nList)):
    # print('i', i)
    countList = []
    
    for j in range(i, -1, -1):
        if len(countList) > 2:
            break
        else:
            if nList[i] == nList[j] and i != j:
                # print(nList[i], nList[j])
                cnt += 1
                break    
            else:
                if nList[j] not in countList:
                    countList.append(nList[j])

print(cnt)
