n = int(input())

a, b = 1, 1
cnt = 2

def pivot(a, b, cnt):
    print(a, b, cnt)
    c = a+b
    if cnt == n:
        print(b)
    else:
        cnt += 1
        a = b
        b = c 
        pivot(a, b, cnt)

pivot(a, b, cnt)