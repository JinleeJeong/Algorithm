n = int(input())
nList = list(map(int,input().split()))
k = int(input())

nIdx = []


for idx, i in enumerate(nList):
    
    if k == i:
        # print(k, i)
        nIdx.append(idx+1)
        
if len(nIdx) == 0:
    print(-1)
else:   
    print(min(nIdx))