n = int(input())
callNumber = list(input().split(' '))
resultNum = 10000
for i in range(0, n):
    if(resultNum > int(callNumber[i])):
        resultNum = int(callNumber[i])

print(resultNum)