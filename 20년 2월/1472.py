n,m = map(int, input().split())

# n이 짝수 일 경우( 2, 3 ) 증가부터
# 4 5 6
# 3 2 1
if n % 2 == 0:
    count = n*m-m+1
    countFlag = True

    for i in range(0, n):
        for j in range(0, m):

            if countFlag:
                print(count, end=" ")
                count += 1
            else:
                print(count, end=" ")
                count -= 1
        
        if(countFlag):
            count -= m+1
        else:
            count -= m-1
        countFlag = not countFlag
    
        print()

# n이 홀수 일 경우( 3, 3 ) 감소부터
# 9 8 7
# 4 5 6
# 3 2 1

else:
    count = n*m
    countFlag = False

    for i in range(0, n):
        for j in range(0, m):

            if countFlag:
                print(count, end=" ")
                count += 1
            else:
                print(count, end=" ")
                count -= 1
        
        if(countFlag):
            count -= m+1
        else:
            count -= m-1
        countFlag = not countFlag
    
        print()

