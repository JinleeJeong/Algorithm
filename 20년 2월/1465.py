n, m = map(int,input().split())

zArray = []
if n == 1 and m == 1 :
    print(1)
else:
    if(n > m):
        idx = n*m
        count = m-1
        # zArray에 역순으로 입력시킨다.
        for i in range(0, n):
            for j in range(0, m):
                zArray.append(idx)
                idx -= 1
        
        # 열이 1이면, 그대로 출력한다
        if m == 1:
            for x in range(0, len(zArray)):
                print(zArray[x])

        # 그 외의 상황이면, count 값이 열로 되어 있기 때문에, 행을 구분 시킨다.
        # pop을 통해서 입력되면, 앞에를 제외시켜서 항상 동일한 배열 상태로 만든다.
        else:
            for x in range(0, len(zArray)):
                if(count == -1):
                    print()
                    count += m
                print(zArray[count], end=" ")
                zArray.pop(count)
                count -= 1
                
    else:

        # index 첫 시작
        index = m*n-m+1
        for i in range(0, n):
            for j in range(0, m):

                print(index, end=" ")
                
                # 맨 뒤 자리 수가 나오면, 맨 앞자리 수를 위해서! 그에 대한 규칙으로 대입
                if(index % m == 0):
                    index -= m*2-1
                else:
                    index += 1
            print()