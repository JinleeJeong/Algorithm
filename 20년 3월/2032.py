k, n = map(int, input().split())

aList = [0] * 100000
bList = [0] * 100000

for i in range(0, n):
    x, y = map(int, input().split())
    aList[i] = x
    bList[i] = y

p = int(input())

for i in range(0, n):
    if aList[i] == p:
        p = bList[i]
    elif bList[i] == p:
        p = aList[i]

print(p)