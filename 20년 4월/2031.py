Excel = list(input())
changerList = []
sumNum = 0

for i in range(len(Excel)-1, -1, -1):
    changerList.append(ord(Excel[i])-64)

k = 1

for i in range(0, len(changerList)):
    sumNum += changerList[i]*k
    k *= 26
print(sumNum)