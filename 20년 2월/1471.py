n = int(input())

nx = 1
ny = 1

for i in range(0, n):
    #Flag와 count로 print 제어

    # 1470 반대 문제
    countFlag = False

    # 4인 경우, 4 > 3 > 2 > 1
    count = n-i

    for j in range(0, n):
        if(countFlag == True):
            # n이 4인경우, 7증가 // 5증가 // 3증가 // 1증가
            print(count, end=" ")
            count += n*2-nx
        
        else:
            # n이 4인경우 1증가 // 3증가 // 5증가 // 7증가
            print(count, end=" ")
            count += ny
        
        countFlag = not countFlag

    nx += 2
    ny += 2

    print()