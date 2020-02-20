n = int(input())
matrix = [[0]*n for i in range(n)]
row, col = map(int, input().split())

# 각 0,0 1,1 2,2를 대입 후에, row col에 따른 값 유추!

def get_number(a, b):
    return (abs(a - (row-1)) + abs(b - (col - 1)) + 1)

for a in range(0, n):
    for b in range(0, n):
        print(get_number(a, b), end=' ')
    print()