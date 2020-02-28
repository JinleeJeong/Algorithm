n = int(input())
nList = list(map(int, input().split()))
k = int(input())

def codeup(nList):
    count = 1
    
    if k not in nList:
        print(-1)
    for i in nList:
        if k == i:
            return print(count)
        else:
            count += 1

codeup(nList)