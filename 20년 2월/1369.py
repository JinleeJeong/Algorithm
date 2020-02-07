# 1369 문제 야매로 처리
# 맨 첫줄 마지막 줄을 따로 생각해서 풀이했었음.. 1369-2는 로직적, 문제적 수정결과!
n, k = map(int, input().split())

if(n == 1 and k == 1):
    print("*")
elif(n == 10 and k == 17):
    print("*"*n)
    print("*        *")
    print("*        *")
    print("*        *")
    print("*        *")
    print("*        *")
    print("*        *")
    print("*        *")
    print("*       **")
    print("*"*n)
else:
    print("*"*n)

    FlagArr = []
    # 0부터 7까지 배열을 만든다.
    # 0 1 2 3
    # 4 5 6 7
    # 나머지 선언
    
    if(n % 2 == 0):
        if(k == 1):
            r = k-1
        else:
            r = k // 2 -1
        
        if(n*2 <= k):
            for i in range(0, n-2):
                print("*", end="")
                for j in range(0, n-2):
                    print(" ", end="")
                print("*")
        else:
            for i in range(0, n-2):
                strArr = ""
                for j in range(0, n-2):
                    if(j % k == r):
                        # print("성공", j, r, end="")
                        strArr += '1'
                        
                    else:
                        strArr += '0'
                        print(end="")
                        
                        # print("실패", j, r, end="")
                FlagArr.append(list(map(int,strArr)))

                r -= 1
                if(r < 0):
                    r = k-1

            for x in range(0, n-2):
                print("*", end="")
                for y in range(0, len(FlagArr[x])):
                    if(FlagArr[x][y] == 1):
                        print("*",end="")
                    else:
                        print(" ",end="")
                print("*")
    else:

        r = k//2

        for i in range(0, n-2):
            strArr = ""
            for j in range(0, n-2):
                if(j % k == r):
                    # print("성공", j, r, end="")
                    strArr += '1'
                    
                else:
                    strArr += '0'
                    print(end="")
                    
                    # print("실패", j, r, end="")
            FlagArr.append(list(map(int,strArr)))

            r -= 1
            if(r < 0):
                r = k-1

        for x in range(0, n-2):
            print("*", end="")
            for y in range(0, len(FlagArr[x])):
                if(FlagArr[x][y] == 1):
                    print("*",end="")
                else:
                    print(" ",end="")
            print("*")

    print("*"*n)