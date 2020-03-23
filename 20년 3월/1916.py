N = int(input())

a, b = 1, 1
cnt = 3
def pivot(a, b):
    
    if N == 1 or N == 2:
        print(1)
    elif N == 3:
        print(2)
    else:
        global cnt
        c = a+b
        a = b
        b = c
        if cnt == N:
            print(c % 10009)
        else:
            cnt += 1
            pivot(a, b)

pivot(a, b)