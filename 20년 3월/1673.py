a, b, c = map(int, input().split())

maxNum = max(a, b, c)

for i in range(maxNum, 0, -1):
    
    if a % i == 0 and b % i == 0 and c % i == 0:
        print(i)
        break