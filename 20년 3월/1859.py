n = int(input())

cnt = 1
def star(cnt):
    if cnt > n:
        return 1
    else:
        print("*"*cnt)
        cnt += 1
        star(cnt)
star(cnt)