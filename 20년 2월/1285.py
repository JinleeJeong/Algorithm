calculator = list(str(input()))

x = 0
numList = []
operatorList = []
num = ''

for i in calculator:
    # i 값이 숫자 값인지 판별 숫자면 True!
    if(i.isdigit()):
        num += i
    else:
    # 숫자가 아니면, 그동안에 더했던 값을 numList에 담고, 초기화
        numList.append(num)
        num = ''
        operatorList.append(i)

resultNum = int(numList[0])

while True:
    if(operatorList[x] == '='):
        break
    else:

        if(operatorList[x] == '+'):
            resultNum += int(numList[x+1])
        elif(operatorList[x] == '-'):
            resultNum -= int(numList[x+1])
        elif(operatorList[x] == '*'):
            resultNum *= int(numList[x+1])
        elif(operatorList[x] == '/'):
            resultNum //= int(numList[x+1])
        x += 1

print(int(resultNum))