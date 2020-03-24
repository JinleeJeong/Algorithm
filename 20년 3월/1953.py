n = int(input())
cnt = 1

def drawing(n):
    global cnt

    if cnt > n:
        return 1
    else:
        print("*"*cnt)
        cnt+=1
        drawing(n)

drawing(n)