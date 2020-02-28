n = int(input())

def codeup(n):
    nSum = 0
    for i in range(1, n+1):
        nSum += i
    
    return nSum

print(codeup(n))