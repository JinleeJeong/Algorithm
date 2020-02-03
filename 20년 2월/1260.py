a,b = map(int,input().split())

result = 0

for i in range(a, b+1):
    if(i % 3 ==0):
        result += i

print(result)