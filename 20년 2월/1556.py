n = int(input())

def codeup(n):
    nFac = 1
    for i in range(n, 0, -1):
        nFac *= i
    return nFac

print(codeup(n))


