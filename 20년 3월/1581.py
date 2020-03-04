def myswap(a, b):
    temp = a
    a = b
    b = temp
    if a < b:
        print(a, b)
    else:
        print(b, a)

a, b = map(int,input().split())

myswap(a,b)