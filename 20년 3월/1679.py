n = int(input())
triFlag = False

for i in range(1, (n//3)+1):
    for j in range(1, (n//2)+1):
        if i+j > n-i-j and i <= j and j <= n-i-j:
            triFlag = True
            print(i,j,n-i-j)

if triFlag == False:
    print("-1")