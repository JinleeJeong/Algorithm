sumNum = int(input())

startNum = 1
resultNum = 0
while resultNum < sumNum:

    resultNum = resultNum + startNum
    startNum = startNum + 1
    
print(startNum - 1)

# 마지막에 1을 더해서 출력되기 때문에, -1을 해줘야 정상적인 값이 출력됀다.