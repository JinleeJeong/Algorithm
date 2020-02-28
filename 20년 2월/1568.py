n = int(input())
nList = list(map(int,input().split()))
a, b = map(int ,input().split())

nNum = nList[a-1]
nIdx = a

if len(nList) == 1:
    print(1)
else:
    for idx, i in enumerate(nList):
        if idx+1 >= a and idx+1 <= b:
            # print('idx+1 : ', idx+1,'i : ', i)
            if nNum < i:
                nIdx = idx+1
                nNum = i
    print(nIdx)