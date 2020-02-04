n,r = map(int,input().split())

nNum = 1
rNum = 1
minusNum = 1

for i in range(n, 0, -1):
    nNum *= i

for j in range(r, 0, -1):
    rNum *= j

for k in range(n-r, 0, -1):
    minusNum *= k
print(int(nNum / (rNum * minusNum)))