w, h = map(int, input().split(" "))
n = int(input())
count = 0
barInfo = []
stage = []
for i in range(0, n):
    barInfo.append(list(map(int, input().split(" "))))

# 여기가 가장 중요, width, height 값이 다를때!! 0,1 -> 0,2 등 가로가 증가 즉 뒤에가 range(0,w)가 되어야 한다!
stage = [[0 for x in range(0, h)] for y in range(0, w)]

for x in range(0, n):
    # x는 전체 3개의 막대를 위한 갯수
        if(barInfo[x][1] == 0): #[x][1]은 첫번째 막대의 가로 세로 구분자
            
            row = barInfo[x][2]
            col = barInfo[x][3]

            for i in range(0, barInfo[x][0]): #[x][0]은 막대의 길이를 말하며, 그에 따라 1의 값을 삽입한다.
                stage[row-1][col-1] = 1
                col += 1
                # 가로의 값을 증가 시키기 위해 col 지역 변수 선언 후 증가
        else:
            row = barInfo[x][2]
            col = barInfo[x][3]

            for i in range(0, barInfo[x][0]): #[x][0]은 막대의 길이를 말하며, 그에 따라 1의 값을 삽입한다.
                stage[row-1][col-1] = 1
                row += 1
                # 세로의 값을 증가 시키기 위해 col 지역 변수 선언 후 증가
for x in range(0, w):
    for y in range(0, h):
        if(x > count):
            print("")
            count += 1
        print(stage[x][y], end =" ")