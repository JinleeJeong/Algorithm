n = int(input())

nNor = n
nList = list(str(n))
nFlag = True

nOpp = []
nOppNum = ''

nResult = 0
nResultList = []

for i in range(len(nList)-1, -1, -1):
    nOpp.append(nList[i])

for i in nOpp:
    nOppNum += i

nOppNum = int(nOppNum)

nResult = nOppNum + nNor
nResultList = list(str(nResult))

for i in range(0, len(nResultList)//2):
    if nResultList[i] != nResultList[len(nResultList)-(i+1)]:
        nFlag = False
        print("NO")
        break

if nFlag:
    print("YES")
