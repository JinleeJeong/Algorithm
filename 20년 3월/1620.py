n = int(input())

nList = list(str(n))
# print('nList : ', nList)
if len(nList) == 1:
    print(n)
else:
    while len(nList) > 1:
        nNum = 0
        for i in range(0, len(nList)):
            # print('nList Int : ', int(nList[i]))
            nNum += int(nList[i])

        nList = list((str(nNum)))
        # print('n : ' ,nNum)
        # print('nList : ', nList)
    print(nNum)
