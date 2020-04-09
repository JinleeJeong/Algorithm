n = int(input())

kaus = n
nList = []
print("{", end="")
while True:
    if kaus % n == 0 and kaus != n:
        break
    else:
        nList.append(kaus)
        kaus += 1
        
for i in range(0, len(nList)):
    if i == len(nList)-1:
        print("%d" %nList[i], end="")
    else:
        print("%d," %nList[i], end=" ")
    
print("}", end="")