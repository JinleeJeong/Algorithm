n, m = map(int, input().split())

zArray = []

for x in range(n*m, 0, -1):
    zArray.append(x)

idx = 0
for i in range(0,n):
    for j in range(0,m):
        # zArray의 최종 idx를 넘어 설 경우
        if idx >= n*m:
            # 뒤에서 앞으로 오기 위한 조건 >> n*m -1을 하게 되면 기준 값에 +1 배열 나타냄!!
            idx -= n*m-1
            print(zArray[idx], end=" ")
            idx += n
        else:
            print(zArray[idx], end=" ")
            idx += n
    print()
