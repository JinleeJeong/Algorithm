n = int(input())

result = 0
for i in range(2, n):
    if((n % i) == 0):
        result = 1
if(result == 1):
    print("not prime")
else:
    print("prime")