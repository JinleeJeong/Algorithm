n = int(input())
nList = list(map(int, input().split()))

print(nList[0], nList[len(nList)//2], nList[len(nList)-1], sep=" ")