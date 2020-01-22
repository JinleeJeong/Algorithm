maxNum = int(input())

i = 1
result = []
while True:
    if(i > maxNum):
        for x in result:
            print(x, end=" ")
        break
    else:
        if(i % 3 != 0):
            result.append(i)
        i = i + 1