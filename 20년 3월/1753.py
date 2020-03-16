n = int(input())

for i in range(0, n):
    nList = list(input())

    for i in range(len(nList)-1, -1, -1):
        print(nList[i], end="")
    
    print()