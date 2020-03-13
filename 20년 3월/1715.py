a, b = map(int, input().split())
forFlag = True

while True:

    if a == 1 or forFlag == False:
        break
    
    for i in range(2, a+1):
        if a % i == 0 and b % i == 0:

            a //= i
            b //= i
            break
        else:
            forFlag = False
print(a, b)