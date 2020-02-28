n, m, x = map(int, input().split())

nList = []
nList.append(n)
nList.append(m)
nList.append(x)

def codeup(nList):
    for i in range(0, len(nList)):
        for j in range(0, len(nList)-1):
            if nList[j] < nList[j+1]:
                nList[j], nList[j+1] = nList[j+1], nList[j]

    return nList
result = codeup(nList)
print(result[1])
