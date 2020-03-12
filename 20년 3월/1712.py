n, m, k = map(int, input().split())

diff = m-n

for i in range(n, k+1, diff):
    print(i, end=" ")