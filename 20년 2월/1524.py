# 지뢰찾기

nList = []

for i in range(0, 9):
    nList.append(list(map(int,input().split())))

# r, c를 받아서, 배열 시작은 0이기 때문에 빼줌
r, c = map(int,input().split())

x = r - 1
y = c - 1
cnt = 0

# 위치가 지뢰이면 -1 출력
if nList[x][y] == 1:
    print(-1)

else:

    # 주변 8칸을 돌기 위한 루트
    x -= 1
    y -= 1
    for i in range(0, 3):
        for j in range(0, 3):
            # x y가 9를 넘는 순간 Listout
            if x < 9 and y < 9:
                # 위가 참이며, 논이 아니고, 0이 아닌 지뢰이면 카운트
                if nList[x][y] != None and nList[x][y] != 0 and x >= 0 and y >= 0:
                    cnt += 1
            y += 1
        y = c - 2
        x += 1
    if cnt == 0:
        print(0)
    else:
        print(cnt)