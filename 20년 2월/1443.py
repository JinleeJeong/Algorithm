n = int(input())
nList = [0 for i in range(0,n)]

for x in range(0, n):
    nList[x] = input()

# 삽입
for i in range(0, n):
    # i == 1 
    # j == 0
    j = i - 1
    key = nList[i]

    # 위 조건 2개 다 만족 시
    while nList[j] > key and j >= 0:
        # j+1에다가 j를 넣은 후, j도 업데이트 필요. 아래의 key 값으로 업데이트 
        nList[j+1] = nList[j]
        j = j - 1

    # nList[j]가 아니다. j = j - 1을 진행하여, 0번째 배열인지 -1번째(while탈출)인지 판단이기 때문에 j+1이다.
    nList[j+1] = key

for y in nList:
    print(y)
