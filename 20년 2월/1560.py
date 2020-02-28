n, m = map(int, input().split())

def codeup(n, m):
    if n > m:
        return n-m
    else:   
        return m-n

result = codeup(n,m)
print(result)