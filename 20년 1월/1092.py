a, b, c = map(int, input().split(" "))
d = 1
while True:
    if(((d % a == 0) and (d % b == 0) and (d % c == 0)) == False):
        d += 1
    else:
        print(d)
        break


# 최소 공배수

# 1. 두 수를 비교해서 낮은 값을 기준으로하고 C값에 대입
# 2. 하나씩 나누었을 때 둘다 나눈 값이 0일 때 까지 C를 하나씩 증가 시킴
