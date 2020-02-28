n = int(input())
nList = list(map(int, input().split()))

def hello(nList):

    minNum = 1000000000

    for i in nList:
        if minNum > i:
            minNum = i

    print(minNum)

hello(nList)