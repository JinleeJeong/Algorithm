n = int(input())
nList = []

for i in range(n):
    nList.append(input())
    if i != n-1:
        nList.append("AMOLED")

for i in nList:
    print(i)