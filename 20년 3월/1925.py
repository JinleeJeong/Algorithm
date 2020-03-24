n, r = map(int, input().split())


def factorial(x, sumNum):
    # print(x, sumNum)
    if x == 1:
        return sumNum
    else:
        sumNum *= x
        x -= 1
        return factorial(x, sumNum)
    
print(factorial(n, 1) // (factorial(r, 1) * factorial(n-r, 1)))