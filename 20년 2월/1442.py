n = int(input())
nList = [0 for i in range(0,n)]

for x in range(0, n):
    nList[x] = input()

# 선택은 0~n-1, i+1, n로 min을 구한다. 
for i in range(0, n-1):
    # 맨 앞의 idx를 잡는다.
    minIdx = i
    for j in range(i+1, n):
        # 맨 앞 제외한 모두를 비교 후, 최소 값을 받은 후
        if nList[minIdx] > nList[j]:
            minIdx = j
    # 항을 파악 후, 정리를 한다.
    nList[i], nList[minIdx] = nList[minIdx], nList[i]

for y in nList:
    print(y)

