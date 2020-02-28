a, b = map(int,input().split())

def codeup(a, b):

    while b:
        a, b = b, a%b
    
    return a

result = a*b // codeup(a, b)
print(result)