N = int(input())

NList = []

for i in range(1, N+1):
    if(N % i == 0):
        NList.append(i)

for j in NList:
    print(j, end=" ")