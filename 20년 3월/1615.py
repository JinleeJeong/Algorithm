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
        
        print('gener : ',gener(i))
        if gener(i):
            
            nList[gener(i)] = 1


    for i in range(a, b):
        if nList[i] == 0:
            selfCount += i

    print(selfCount)