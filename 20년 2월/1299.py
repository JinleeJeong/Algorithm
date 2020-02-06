a,b,c = map(int, input().split())

x = -1000
y = -1000
resultFlag = False

for i in range(0, 10000):
    for j in range(0, 10000):
        if(resultFlag == True):
            break
        if(a*i + b*j == c):
            print(i, j, sep=" ")
            resultFlag = True
        
