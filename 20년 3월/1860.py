n = int(input())

def triangle(k, t):

    if k == 1:
        print(k, end=" ")
        return
    if t == 1:
        triangle(k-1, k-1)
        print()
    else:
        triangle(k, t-1)
    
    print(t, end=" ")
    return

triangle(n, n)