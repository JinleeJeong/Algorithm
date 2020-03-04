loop = int(input())

for i in range(0, loop):
    n = int(input())
    nList = list(str(n))
    if len(nList) == 1:
        
        print(n)
    else:
        while len(nList) > 1:
            nNum = 0
            for i in range(0, len(nList)):
            
                nNum += int(nList[i])

            nList = list((str(nNum)))
        print(nNum)
