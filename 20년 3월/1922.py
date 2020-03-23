n = int(input())

cnt = 1

def cycle(n):
    global cnt
    if n == 1:
        print(cnt)
    elif n % 2 == 1:
        cnt += 1
        n = 3*n + 1
        cycle(n)
    else:
        cnt += 1
        n //= 2 
        cycle(n)

cycle(n)