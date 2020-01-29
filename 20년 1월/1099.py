stage = []
count = 0

# 10 X 10 의 이차원 배열 선언
for x in range(0, 10):
    stage.append(list(map(int, input().split(" "))))

# row와 col은 1과 1부터 비교 각 테두리는 1값 체크 X
row = 1
col = 1

for i in range(0, 10):
    for j in range(0, 10):
        # print(row, col)

        # 1인 경우 & row가 9가 안넘은 경우에는 행 증가 / 열 감소(이전상태)
        if(stage[row][col] == 1):
            # print("if 경우", stage[row][col])

            if(row != 9):
                row += 1
                col -= 1
            else:
                col = 0
        
        # 0인 경우 & col가 9가 안넘은 경우에는 열 증가
        elif(stage[row][col] == 0):
            # print("elif 경우", stage[row][col])

            stage[row][col] = 9
            if(col != 9):
                col += 1
            else:
                col = 0
        
        # 예외 인 경우 9로 변환 후 종료
        else:
            # print("else 경우", stage[row][col])

            stage[row][col] = 9




# 출력 루틴
for i in range(0, 10):
    for j in range(0, 10):
        if(i > count):
            print("")
            count += 1
        print(stage[i][j], end= " ")