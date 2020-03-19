# nCr 문제

n, r = map(int, input().split())

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)
if n == r:
    print(1)
elif n < r:
    print(0)
else:   
    print(factorial(n) // (factorial(n-r) * factorial(r)))