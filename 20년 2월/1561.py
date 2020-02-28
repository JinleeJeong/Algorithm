n, m = map(int, input().split())

def codeup(n, m):
    if n > m:
        return n
    else:   
        return m

result = codeup(n,m)
print(result)