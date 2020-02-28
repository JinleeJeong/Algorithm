n = list(input())

def codeup(n):
    if n == 1:
        return print(1)
        
    for i in range(0, len(n)):
        n[i] = int(n[i])

    for i in range(len(n)-1, -1, -1):
        print(n[i], end="")

codeup(n)