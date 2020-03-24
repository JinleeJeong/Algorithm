n = int(input())
nList = []


def threeN(n):
    nList.append(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        n //= 2
        threeN(n)
    else:
        n *= 3
        n += 1
        threeN(n)

def Reverse(nList):
    global listIndex
    # print(nList, listIndex)

    if listIndex < 0:
        return 1
    else:
        print(nList[listIndex])
        listIndex -= 1
        Reverse(nList)

threeN(n)
listIndex = len(nList)-1
Reverse(nList)
