n = int(input())

numList = []
iFlag = True

# 6을 2*3 형태로 만들되, 그의 값은 소수여야 한다. 그래서 2, 3은 소수이기 때문에 포함 시켜야한다.
# 한쪽만 2,3 경우에는 소수 인정, 반대쪽은 2, 3으로 나눠져서는 안됀다.(그래야 소수)
# 둘다 2,3이 아닌 경우에는 둘다 2, 3으로 나눠져서는 안됀다. 
for i in range(2, n):
    dividedNum = int(n/i)
    if(n%i == 0):
        if((i == 2 or i == 3) and (dividedNum % 2 != 0 and dividedNum % 3 != 0)):
            numList.append([i, dividedNum])
        elif((i % 2 != 0 and i % 3 != 0) and (dividedNum == 2 or dividedNum == 3)):
            numList.append([i, dividedNum])
        elif((i % 2 != 0 and i % 3 != 0) and (dividedNum % 2 != 0 and dividedNum % 3 != 0)):
            numList.append([i, dividedNum])
        elif((i == 2 or i == 3) and (dividedNum == 2 or dividedNum == 3)):
            numList.append([i, dividedNum])
if(len(numList) > 0):
    print(numList[0][0], numList[0][1])
else:
    print("wrong number")