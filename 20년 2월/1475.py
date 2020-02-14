n,m = map(int, input().split())



# m이 1이면 거꾸로 쭉 나열
if m == 1:
    count = 1
    for i in range(0,n):
        for j in range(0,m):
            print(count)
            count += 1
else:
        
    nx = 1
    ny = 1
    # m이 홀수 인 경우!!
    # 20 13 12 5 4
    # 19 14 11 6 3
    # 18 15 10 7 2
    # 17 16 9 8 1

    # 17 16 9 8 1
    # 18 15 10 7 2
    # 19 14 11 6 3
    # 20 13 12 5 4

    if m % 2 == 1:
        for i in range(0, n):
        #Flag와 count로 print 제어

            countFlag = False
            count = n*m-n+1+i

            for j in range(0, m):
                if(countFlag == True):
                    
                    print(count, end=" ")
                    count -= n*2-nx
                
                else:
                    
                    print(count, end=" ")
                    count -= ny
                
                countFlag = not countFlag

            nx += 2
            ny += 2

            print()
    
    # m이 짝수 인 경우!!
    # 10 9 4 3
    # 11 8 5 2
    # 12 7 6 1


    # 12 7 6 1
    # 11 8 5 2
    # 10 9 4 3
    else:

        nx = 1
        ny = 1

        for i in range(0, n):
        #Flag와 count로 print 제어

            countFlag = True
            count = n*m-i

            for j in range(0, m):
                if(countFlag == True):
                    
                    print(count, end=" ")
                    count -= n*2-nx
                
                else:
                    
                    print(count, end=" ")
                    count -= ny
                
                countFlag = not countFlag

            nx += 2
            ny += 2

            print()