n = int(input())

cnt = n
def opposite(cnt):
    if cnt >= 1:
        print(cnt)
        cnt -= 1
        opposite(cnt)

opposite(cnt)