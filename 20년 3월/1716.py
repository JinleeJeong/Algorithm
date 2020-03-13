n, m = map(int,input().split())

nSum = 0
mSum = 30-m

for i in range(n, 10):
    if i >= 10:
        break
    else:
        if i % 2 == 0:
            nSum += 30
        else:
            nSum += 31


print(nSum+mSum)