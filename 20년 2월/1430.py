n = int(input())
nList = input().split()
m = int(input())
mList = input().split()

for i in range(0, len(mList)):
    if(mList[i] in nList):
        print(1, end=" ")
    else:
        print(0, end=" ")
