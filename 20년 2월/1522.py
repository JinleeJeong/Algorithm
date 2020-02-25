# 와드 설치 문제

# [2][2]부터 시작하고 뒤에는 생각하지 않음
# 이유 : 0, 0이면 음수 값이 나오므로, List 에러
# 와드가 5X5로 퍼짐

nList = [[0]*(15) for i in range(0,15)]

cnt = 0
# 와드가 부쉬 안에 박힌 경우 부쉬 모두 밝힘
flag = False
a1, a2 = map(int, input().split())

# 입력 시, 1 줄여서 나오고 2,2부터 시작이므로 +1만 적용
x = a1 + 1
y = a2 + 1

nList[x][y] = 1

# 5X5를 위함
x -= 2
y -= 2

# 와드 박기
for i in range(0, 5):
    for j in range(0, 5):
        # print(x, y, nList[x][y])
        if nList[x][y] != 1:    
            nList[x][y] = 2
        y += 1
    y = a2 - 1
    x += 1


b1, b2 = map(int, input().split())

x = b1 + 1
y = b2 + 1

nList[x][y] = "a"
x -= 2
y -= 2

# 렌즈 박기
for i in range(0, 5):
    for j in range(0, 5):
        # print(x, y, nList[x][y])
        if nList[x][y] != "a":    
            if nList[x][y] == 2 or nList[x][y] == 1:
                nList[x][y] = "c"
            else:
                nList[x][y] = "b"
        y += 1
    y = b2 - 1
    x += 1

c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())

a = c1 + 1
b = c2 + 1
c = d1 + 1
d = d2 + 1

# 부쉬 위치 확인! 만약 부쉬 안에 와드가 없다면, 1&2의 값만 덧셈
# 아니면 숫자 덧셈
for i in range(a, c+1):
    for j in range(b, d+1):
        if nList[i][j] == 1:
            nList[i][j] = 4
            flag = True
        else:
            if type(nList[i][j]) == int:
                nList[i][j] = 3


for i in range(2, 11):
    for j in range(2, 11):
        # print(nList[i][j], end=" ")
        if flag == True:
            if type(nList[i][j]) == int and nList[i][j] > 0:
                cnt += 1
        else:
            if nList[i][j] == 1 or nList[i][j] == 2:
                cnt += 1  
    # print()          
print(cnt)