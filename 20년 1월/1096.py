n = int(input())

selectArray = []
count = 0
# 바둑판 흰돌 채우는 배열 만들기
for x in range(n):

    x, y = map(int, input().split(" "))
    selectArray.append([x, y])

print(selectArray)

# 바둑판 배열 만들기
stage = [[0 for x in range(0, 19)] for y in range(0, 19)]

# 바둑판에 흰돌 채우기
for i in range(n):
    a = selectArray[i][0]
    b = selectArray[i][1]
    
    stage[a-1][b-1] = 1

# 출력하기
for i in range(0, 19):
    for j in range(0, 19):
        if(i > count):
            print("")
            count += 1
        print(stage[i][j], end=" ")