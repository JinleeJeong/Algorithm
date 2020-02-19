n = int(input())

count = 0
initial = 1
for i in range(1, n+1):
    count = initial
    for j in range(1, n+1):
        print(count, end=" ")
        count += n
    initial += 1
    print()

