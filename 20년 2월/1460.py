n = int(input())

nList = [i for i in range(1,(n*n)+1)]

for i in nList:
    if(i % n == 0 and i != n*n):
        print(i)
    else:
        print(i, end=" ")