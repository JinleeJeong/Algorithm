# 마름모 그리기 - 4개의 변으로 나눠서 계산 필요!!
          
a = int(input())
b = [[' ']*1000 for i in range(1000)]
c = a-1

for i in range(a*2):
    for j in range(a*2):
        # 왼쪽 위 오른쪽 위 왼쪽 아래 오른쪽 아래 순서 
        if i+j+1 == a or j-i == a or ((i-j) == a) or i+j+1 == 3*a:
            # print(i,j)
            b[i][j] = '*'

for i in range(a*2):
    for j in range(a*2):
        print(b[i][j], end="")
    print()