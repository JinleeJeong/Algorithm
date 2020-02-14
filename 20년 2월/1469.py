n = int(input())

count = n + 1
countFlag = False

for i in range(0, n):
    for j in range(0, n):
        if(countFlag == True):
            print(count, end=" ")
            count += 1
            
        else:
            count -= 1
            print(count, end=" ")
            
    print()
    count += n
    countFlag = not countFlag