# 27로 하는 이유는 i-1 j-1과 i+1 j+1을 하게 되면 List out 예외가 출력되기 때문! out된 값들은 어차피 0 영향 X
nList = [[0]*27 for i in range(27)]
mList = [[0]*27 for i in range(27)]

for i in range(1, 26):
    sup = list(map(int, input().split()))
    for j in range(0, 25):
        nList[i][j+1] = sup[j]
        
for i in range(1, 26):
    for j in range(1, 26):
        life = nList[i-1][j-1] + nList[i][j-1] + nList[i+1][j-1] + nList[i-1][j] + nList[i+1][j] + nList[i-1][j+1] + nList[i][j+1] + nList[i+1][j+1]
        if nList[i][j] == 0:
            if life == 3:
                mList[i][j] = 1 
            else:
                mList[i][j] = 0
        else:
            if life == 2 or life == 3:
                mList[i][j] = 1 
            else: 
                mList[i][j] = 0

for i in range(1, 26):
    for j in range(1, 26):
        print(mList[i][j], end=' ')
    print()