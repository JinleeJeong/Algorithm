n = int(input())

nList = list(map(int, input().split()))

for idx, value in enumerate(nList):
    print(idx+1, ":", sep="", end=" ")
    for j in range(0, n):
        if idx != j:
            if value < nList[j]:
                print("<", end=" ")
            elif value > nList[j]:
                print(">", end=" ")
            else:
                print("=", end=" ")
    print()
            