# 크기가 n인 1차원 배열 d[]에 대해

# k개의 구간 [s, e]와 u를 입력 받아,

# d[s] = d[s]+u;
# d[e+1] = d[e+1]-u;

# 를 수행한 후, 누적 합을 만들어 출력해보자.

# 크기가 7이고,

# 4개의 구간 데이터
# 1 2 1
# 2 3 1
# 3 4 1
# 4 5 1

# 가 입력되면

# 1차원 배열의 상태는 
# 1 1 0 0 –1 –1 0
# 가 되며

# 그 누적합을 계산하면 아래와 같다.
# 1 2 2 2 1 0 0

n, k = map(int,input().split())

# List는 0부터 시작하고, e는 1부터 이며 +1까지 이므로, 2로 nList 적용
nList = [0] * (n+2)
count = 0

for i in range(0, k):
    s, e, u = map(int, input().split())
    
    nList[s] += u
    nList[e+1] -= u

for j in range(1, n+1):
    print(nList[j], end=" ")
    
print()
for i in range(0, len(nList)):
    if i == 0:
        count += nList[i]
    else:
        nList[i] += count
        count = nList[i]

for j in range(1, n+1):
    print(nList[j], end=" ")