# 넥슨 입사 시험 
# 셀프 넘버
# 제너레이터 되는 것을 배열에 채워 안채워진 값의 합 더하기

a, b = map(int ,input().split())

nList = [0] * 5000
selfCount = 0

def gener(n):
    num = n

    while n:
        num += n % 10
        n /= 10
    return int(num)

if a == 1 and b == 1:
    print(1)
else:
    for i in range(1, b):
        
        if gener(i):    
            nList[gener(i)] = 1

    for i in range(a, b):
        if nList[i] == 0:
            selfCount += i

    print(selfCount)