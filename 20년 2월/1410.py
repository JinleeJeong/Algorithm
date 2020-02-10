listArr = list(input())

leftCount = 0
rightCount = 0

for i in listArr:
    if(i == '('):
        leftCount += 1
    if(i == ')'):
        rightCount += 1

print(leftCount, rightCount, sep=" ")