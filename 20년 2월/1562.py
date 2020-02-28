n, m = map(int, input().split())

def codeup(n, m):
    if n > m:
        return m
    else:   
        return n

result = codeup(n,m)
print(result)