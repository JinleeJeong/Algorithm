n, c = map(int, input().split())

nList = list(map(int,input().split()))

# sort으로 오름차순 정렬한다.
nList.sort()
for i in range(0, len(nList)):
    # 만약 4명씩 줄 세우는데, 그 값보다 낮으면 그냥 출력
    if(len(nList) < c+1):
        print(nList[i], end=" ")
    
    else:
        # (순번+1)%c를해서 4명씩 세운다면, 4, 8로 줄 바꿈!
        if((i+1)%c == 0):
            print(nList[i], ' ', sep="")
        else:
            # 맨 마지막에 공백을 위한 조건문
            if(i == len(nList)-1):
                print(nList[i], end=" ")
            else:
                print(nList[i], end=" ")

