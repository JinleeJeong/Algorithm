a,b,c,n = map(int, input().split())

result = a

for i in range(0, n-1):
    result = result*b + c

print(result)