n = int(input())

def codeup(n):
    nCount = 0
    for i in range(1, n+1):
        if n % i == 0:
            nCount+= 1
    return nCount

print(codeup(n))


