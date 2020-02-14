n, m = map(int,input().split())

multi = n * m

for i in range(0, n):
    for j in range(0, m):
        print(multi, end=" ")
        multi -= 1
    print()