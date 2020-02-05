a,b,c = map(int,input().split())

bestNum = 0

rangeNum = 0
if(a < b):
    if(a < c):
        rangeNum = a
    else:
        rangeNum = c
else:
    if(b < c):
        rangeNum = b
    else:
        rangeNum = c

for i in range(1, rangeNum+1):
    if(a % i == 0 and b % i == 0 and c % i == 0):
        bestNum = i

print(bestNum)