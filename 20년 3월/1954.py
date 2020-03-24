n = int(input())
cnt = n

def drawing(n):
    global cnt

    if cnt == 0:
        return 1
    else:
        print("*"*cnt)
        cnt-=1
        drawing(n)

drawing(n)