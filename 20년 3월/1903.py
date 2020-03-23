a, b = map(int, input().split())
cnt = a

def odd(cnt):
    if cnt % 2 != 0 and cnt <= b:
        print(cnt)
        cnt += 2
        odd(cnt)
    elif cnt <= b:
        cnt += 1
        odd(cnt)
odd(cnt)