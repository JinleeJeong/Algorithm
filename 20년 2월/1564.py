a, b = map(int,input().split())

def codeup(a,b):

    if a == 1 or b == 1:
        return 1
    
    for i in range(a, 0, -1):
        if a%i == 0 and b % i == 0:
            return i
        
result = codeup(a,b)

print(result)