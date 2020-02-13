n = int(input())

nVar = n

if(n == 1):
    print(1)
while nVar <= n*n and n != 1:
    if(nVar % n == 1):
        print(nVar)
        nVar += n*2 - 1
    else:
        print(nVar, end=" ")
        nVar -= 1