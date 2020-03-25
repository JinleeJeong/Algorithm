pList = []
jList = []

for i in range(3):
    pList.append(int(input()))

for j in range(2):
    jList.append(int(input()))

pMin = min(pList)
jMin = min(jList)

print("%.1f" %(pMin+jMin + (pMin+jMin) / 10))