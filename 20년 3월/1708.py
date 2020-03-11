n = int(input())
nList = list(map(int, input().split()))

for i in range(0, n):
    
    cnt = 1
    for j in range(0, n):
        if nList[i] < nList[j]:
            cnt+=1
    
    print(nList[i], cnt)
    