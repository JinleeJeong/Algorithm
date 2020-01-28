n = int(input())

callNumber = list(input().split(' '))
resultArray = [0] * 24

for i in range(1, 24):
    resultArray[i-1] += callNumber.count(str(i))

for i in range(23):
    print(resultArray[i], end=" ")

# 배열에 하나씩 배치하는 로직 > 기본 24개