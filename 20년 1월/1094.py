n = int(input())

callNumber = list(input().split(' '))
resultArray = []

for i in range(1, n+1):
    resultArray.append(callNumber[i-1])

for i in range(n-1, -1, -1):
    print(resultArray[i], end=" ")

# 거꾸로 배열하는 로직