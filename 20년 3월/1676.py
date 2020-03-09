n = int(input())
nList = list(map(int,input().split()))

copyList = nList
nList = sorted(nList,reverse=True)
overList = {}
rank = 1

while len(nList) > 0:

    for idx, value in enumerate(copyList): # 100 80 90 
                                            # 100 90 80 nList
        if len(nList) == 0:
            break
        # print('idx, value : ', idx, value)
        # print('nList : ', nList)
        # print('info : ',nList[0], value, overList)

        if nList[0] not in overList.values():
            if nList[0] == value:
                print(idx+1)

                overList = {"idx" : idx+1, "n" : nList[0]}
                nList.pop(0)
        else:
            if nList[0] == value:
                print(overList.get("idx"))
                nList.pop(0)