n = int(input())
nList = list(map(int, input().split()))

def solution(nList):
    k = 0
    
    for i in range(n):
        changeFlag = False

        for j in range(n-1):
            if nList[j] > nList[j+1]:
                nList[j], nList[j+1] = nList[j+1], nList[j]
                changeFlag = True

        if changeFlag == False:
            k = i
            break

    return k    

print(solution(nList))