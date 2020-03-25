import math

b,n=map(int,input().split())
a = 0

# 충분히 돌 수 있도록 한다.
for i in range(1, b):

    # i의 n승이 b보다 커지거나 같을 때를 캐치!
    if pow(i, n) >= b:
        a = i
        break

# 비슷하지만, +1이였기 때문에, 작은 값도 비교해본다.
# print(a)
if pow(a, n) -b >= b - pow(a-1,n):
    a -= 1

if n == 1 or b == 1:
    print(b)
else:
    print(a)