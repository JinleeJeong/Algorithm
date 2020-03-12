a, b = map(int, input().split())
forFlag = True

while True:
    print("Entry")
    if a == 1 or forFlag == False:
        print("??")
        break
    
    for i in range(2, a+1):
        print(a, b, i)
        if a % i == 0 and b % i == 0:
            print(a, b)

            a //= i
            b //= i
            break
        else:
            forFlag = False
print(a, b)