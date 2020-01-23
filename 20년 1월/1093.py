n = int(input())

callNumber = list(input().split(' '))
resultArray = [0] * 24

for i in range(1, 24):
    resultArray[i-1] += callNumber.count(str(i))

for i in range(23):
    print(resultArray[i], end=" ")
