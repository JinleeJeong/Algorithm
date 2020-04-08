a, b = map(int, input().split())

check = a*a - 4*b
printFlag = False

if check > 0:
    for i in range(-100, 101):
        for j in range(-100, 101):
            if i + j == a and i * j == b and printFlag == False:
                if i > 0 :
                    print("x+%d" %i)
                else:
                    print("x%d" %i)
                if j > 0 :
                    print("x+%d" %j)
                else:
                    print("x%d" %j)
                printFlag = True

elif check == 0:
    for i in range(-100, 101):
        for j in range(-100, 101):
            if i + j == a and i * j == b and printFlag == False:
                if i > 0 :
                    print("x+%d" %i)
                else:
                    print("x%d" %i)
                printFlag = True
else:
    print(-1)