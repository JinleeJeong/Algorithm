n, g = map(int, input().split())
nList = list(map(int, input().split()))

# nList와 g값이 맞지 않아서 배열의 Listout 문제 해결 작은 값 뽑기!!
while len(nList) % g != 0:
    nList.append(1000)

resultList = []
x = 0

# 입력 값이 3 이상인 경우
if n >= 3:
    # 0~n까지 이지만, g로 띔
    for i in range(0, n, g):
        minVar = 1001
        # g가 3이면 i도 0, 3으로 진행 그리고 i+g로 3개의 값씩 비교
        for j in range(i, i+g):
            if minVar > nList[j]:
                minVar = nList[j]
        resultList.append(minVar)

# 입력 값이 2 이하인 경우에는 한번만 하기 때문에 그대로 비교
else:
    for i in range(0, n, g):
        minVar = 1001
        for j in nList:
            if minVar > j:
                minVar = j
        resultList.append(minVar)

for i in resultList:
    print(i, end=" ")