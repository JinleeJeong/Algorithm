# 크레이지 아케이드 문제

nList = []
nObj = []

# 10개의 배열을 받음
for i in range(10):
    nList.append(list(map(int,input().split())))

# 배열을 돌면서 물풍선을 찾은 후, i, j, key(범위) 저장
for i in range(10):
    for j in range(10):
        if nList[i][j] > 0:
            nObj.append({
                'key' : nList[i][j],
                'i' : i,
                'j' : j
            })

# 10 X 10 배열 물풍선 영향 반영
for x in range(0, len(nObj)):
    
    aVar = nObj[x].get('i')
    bVar = nObj[x].get('j')

    aaVar = nObj[x].get('i')
    bbVar = nObj[x].get('j') 

    # 가로로 감소 > 현위치 > 증가 순서
    for i in range(0, nObj[x].get('key')*2+1):

        # 감소 시, -1 발견하면 그대로 continue
        if i < (nObj[x].get('key')*2+1) // 2:
            if nList[aVar][bVar] == -1:
                continue

            else:
                bVar -= 1
                if bVar < 0:
                    bVar = 0
        # 초기화
        elif i == (nObj[x].get('key')*2+1) // 2:
            bVar = nObj[x].get('j')

        # 증가
        else:

            if nList[aVar][bVar] == -1:
                continue
            else:
                bVar += 1
                if bVar > 9:
                    break
        
        # 위에 처리 후 대입
        if bVar >= 0:
            if nList[aVar][bVar] != -1:
                nList[aVar][bVar] = -2 

    # 세로로 감소 > 현위치 > 증가 순서
    for j in range(0, nObj[x].get('key')*2+1):
        if j < (nObj[x].get('key')*2+1) // 2:
            
            # 감소 시, -1 발견하면 그대로 continue
            if nList[aaVar][bbVar] == -1:
                continue

            else:
                aaVar -= 1
                if aaVar < 0:
                    aaVar = 0

        # 초기화
        elif j == (nObj[x].get('key')*2+1) // 2:
            aaVar = nObj[x].get('i')
            
        # 증가
        else:

            if nList[aaVar][bbVar] == -1:
                continue
            else:
                aaVar += 1
                if aaVar > 9:
                    break
        
        # 위에 처리 후 대입
        if aaVar >= 0:
            if nList[aaVar][bbVar] != -1:
                nList[aaVar][bbVar] = -2 


n = int(input())

# 플레이어 입력받음
playList = []
for i in range(n):
    playList.append(list(map(int, input().split())))

# 플레이어 idx를 받으면서, 플레이 리스트가 죽었는지 판단! 살았으면 nList에 대입
for idx, x in enumerate(range(0, len(playList))):
    if nList[playList[x][0]-1][playList[x][1]-1] != -2:
        nList[playList[x][0]-1][playList[x][1]-1] = idx + 1


for i in range(10):
    for j in range(10):
        print(nList[i][j], end=" ")
    print()

print("Character Information")
for idx, x in enumerate(range(0, len(playList))):
    if nList[playList[x][0]-1][playList[x][1]-1] == -2:
        print("player", idx+1, "dead", sep=" ")
    else:
        print("player", idx+1, "survive", sep=" ")
