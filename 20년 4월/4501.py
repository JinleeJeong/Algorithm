nList = []

for i in range(7):
    nList.append(int(input()))

nList = sorted(nList, reverse=True)

print(nList[0])
print(nList[1])