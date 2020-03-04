def mysubstr(strA, startNum, countNum):
    strA = list(strA)
    for i in range(startNum, countNum):
        print(strA[i], end="")

strA = input()
sN, cN = map(int, input().split())
cN += sN
mysubstr(strA, sN, cN)