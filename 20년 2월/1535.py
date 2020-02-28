n = int(input())
nList = list(map(int, input().split()))

def hello(nList):

    if n == 1:
        print(1)
    
    else:
        maxNum = 0
        maxIdx = 0
        for idx, i in enumerate(nList):
            if maxNum < i:
                maxIdx = idx + 1
                maxNum = i

        print(maxIdx)

hello(nList)