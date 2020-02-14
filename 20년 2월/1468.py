n = int(input())

count = 0
countFlag = True

for i in range(0, n):
    for j in range(0, n):
        if(countFlag == True):
            count += 1
            print(count, end=" ")
            
        else:
            print(count, end=" ")
            count -= 1
    print()
    count += n
    countFlag = not countFlag