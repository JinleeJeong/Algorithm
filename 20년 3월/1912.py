n = int(input())

cnt = n
multiNum = 1

def factorial(cnt):
    global multiNum
    if cnt >= 1:
        multiNum *= cnt
        cnt -= 1
        factorial(cnt)

factorial(cnt)
print(multiNum)