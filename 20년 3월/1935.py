a, b = map(int ,input().split())
cnt = 0
def eZin(a, b):
    global cnt
    if a == b:
        return a
    elif a > b:
        cnt += 1
        return eZin(a//2, b)
    else:
        cnt += 1
        return eZin(a, b//2)
    
eZin(a,b)
print(cnt)