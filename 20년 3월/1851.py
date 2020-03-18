n = int(input())

def starPrint(n):
    if n == 0:
        return 0
    else:
        print("*", end="")
        n -= 1
        starPrint(n)
    
starPrint(n)
